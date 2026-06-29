"""
Progress Tracker CLI — manage participants, homework, and submissions from
the terminal. Designed for the AI Consultant Bootcamp facilitator.

Examples:
  # Enroll a participant
  python3 -m engine.progress_cli enroll "Michael Brave" michael@example.com

  # Show current progress dashboard
  python3 -m engine.progress_cli status michael-b-2026

  # Mark a homework as in-progress, submitted, or approved
  python3 -m engine.progress_cli start michael-b-2026 phase-1-week-1-hw1
  python3 -m engine.progress_cli submit michael-b-2026 phase-1-week-1-hw1 \\
      --evidence https://github.com/mbgulden/belief-deprogrammer/pull/42
  python3 -m engine.progress_cli approve michael-b-2026 phase-1-week-1-hw1

  # Bulk-load the Phase 1 curriculum (idempotent)
  python3 -m engine.progress_cli seed phase-1

  # List overdue homework
  python3 -m engine.progress_cli overdue
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# Allow `python3 -m engine.progress_cli` from project root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine.progress_tracker import (  # noqa: E402
    Homework,
    ProgressStore,
    Submission,
    _today_iso,
    _utcnow_iso,
)


DEFAULT_DB = Path(__file__).resolve().parent.parent / "data" / "progress.json"


# ---------- Phase 1 curriculum (GRO-499 → GRO-502) ---------------------------

PHASE_1_CURRICULUM: list[Homework] = [
    Homework(
        id="phase-1-week-1-hw1",
        phase="phase-1", week=1,
        title="Curate YouTube Expert Library (15-25 videos)",
        deliverable="Spreadsheet / markdown list with URL, expert, why-it-matters, watched/not",
        due_days=7, weight=2,
    ),
    Homework(
        id="phase-1-week-1-hw2",
        phase="phase-1", week=1,
        title="Design HD-Tailored Self-Coaching Curriculum",
        deliverable="Lesson plan: 8-12 modules, each with HD gate/center hook + workbook tie-in",
        due_days=7, weight=3,
    ),
    Homework(
        id="phase-1-week-2-hw1",
        phase="phase-1", week=2,
        title="Build Progress Tracker and Homework System",
        deliverable="This CLI + JSON store + tests passing locally",
        due_days=14, weight=2,
    ),
    Homework(
        id="phase-1-week-2-hw2",
        phase="phase-1", week=2,
        title="Execute Week 1 — C-Suite Communication",
        deliverable="3 outbound messages to C-suite targets (CEO/COO/Head of People) with reply log",
        due_days=14, weight=3,
    ),
]


# ---------- Handlers ----------------------------------------------------------

def cmd_enroll(args, store: ProgressStore) -> int:
    p = store.add_participant(args.name, args.email, args.id or "")
    print(f"✅ enrolled {p.name} as {p.id} (started {p.started_at})")
    return 0


def cmd_list_participants(args, store: ProgressStore) -> int:
    rows = store.list_participants()
    if not rows:
        print("(no participants enrolled yet)")
        return 0
    print(f"{'id':<30} {'name':<24} {'phase':<10} {'week':<5} {'started':<22}")
    print("-" * 90)
    for p in rows:
        print(f"{p['id']:<30} {p['name']:<24} {p['current_phase']:<10} {p['current_week']:<5} {p['started_at']:<22}")
    return 0


def cmd_seed(args, store: ProgressStore) -> int:
    if args.phase != "phase-1":
        print(f"❌ seed only implemented for phase-1 (asked for {args.phase})", file=sys.stderr)
        return 2
    added = store.bulk_add_homework(PHASE_1_CURRICULUM)
    print(f"✅ phase-1 curriculum loaded ({added} new homework items, "
          f"{len(PHASE_1_CURRICULUM) - added} already present)")
    return 0


def cmd_status(args, store: ProgressStore) -> int:
    pid = args.participant
    p = store.get_participant(pid)
    if p is None:
        print(f"❌ participant {pid!r} not found", file=sys.stderr)
        return 2
    rows = store.homework_for(pid, phase=p["current_phase"])
    pct = store.completion_pct(pid, phase=p["current_phase"])
    print(f"📊 {p['name']} ({p['id']})")
    print(f"   phase: {p['current_phase']}  week: {p['current_week']}  "
          f"started: {p['started_at'][:10]}  completion: {pct}%")
    print()
    print(f"   {'status':<13} {'due':<12} {'id':<32} {'title':<48}")
    print("   " + "-" * 110)
    for hw, sub in rows:
        status = (sub["status"] if sub else "not_started")
        due = hw["due_days"] and store._due_date(p["started_at"], hw["due_days"]) or "—"
        title = hw["title"][:48]
        print(f"   {status:<13} {due:<12} {hw['id']:<32} {title:<48}")
    nxt = store.next_action(pid)
    if nxt:
        print()
        print(f"   → next: {nxt['homework']['id']}  "
              f"(due {nxt['due_date'] or '—'}, reason: {nxt['reason']})")
    return 0


def _transition(store: ProgressStore, pid: str, hid: str, *, to_status: str,
                evidence: str = "", notes: str = "", reviewer: str = "") -> int:
    if store.get_participant(pid) is None:
        print(f"❌ participant {pid!r} not found", file=sys.stderr)
        return 2
    if not any(h["id"] == hid for h in store.list_homework()):
        print(f"❌ homework {hid!r} not in curriculum (run `seed phase-1` first?)", file=sys.stderr)
        return 2
    existing = next((s for s in store.list_submissions(pid) if s["homework_id"] == hid), None)
    sub = Submission(
        participant_id=pid, homework_id=hid, status=to_status,
        started_at=existing["started_at"] if existing else _utcnow_iso(),
        submitted_at=_utcnow_iso() if to_status in ("submitted", "approved", "rejected") else (existing["submitted_at"] if existing else ""),
        reviewed_at=_utcnow_iso() if to_status in ("approved", "rejected") else (existing["reviewed_at"] if existing else ""),
        reviewer=reviewer or (existing["reviewer"] if existing else ""),
        evidence=evidence or (existing["evidence"] if existing else ""),
        notes=notes or (existing["notes"] if existing else ""),
    )
    store.upsert_submission(sub)
    if to_status == "approved":
        store.record_milestone(pid, "homework-approved", hid)
    print(f"✅ {pid} / {hid} → {to_status}")
    return 0


def cmd_start(args, store): return _transition(store, args.participant, args.homework, to_status="in_progress")
def cmd_submit(args, store):
    return _transition(store, args.participant, args.homework, to_status="submitted", evidence=args.evidence or "", notes=args.notes or "")
def cmd_approve(args, store):
    return _transition(store, args.participant, args.homework, to_status="approved", reviewer=args.reviewer, notes=args.notes or "")
def cmd_reject(args, store):
    return _transition(store, args.participant, args.homework, to_status="rejected", reviewer=args.reviewer, notes=args.notes or "")


def cmd_overdue(args, store) -> int:
    rows = store.overdue()
    if not rows:
        print("🟢 nothing overdue")
        return 0
    today = _today_iso()
    print(f"🔴 {len(rows)} overdue item(s) as of {today}")
    print(f"   {'participant':<26} {'homework':<28} {'status':<13} {'due':<12}")
    print("   " + "-" * 85)
    for p, hw, sub, due in rows:
        print(f"   {p['id']:<26} {hw['id']:<28} {sub['status']:<13} {due:<12}")
    return 0


def cmd_dump(args, store) -> int:
    data = {
        "schema_version": store.SCHEMA_VERSION,
        "participants": store.list_participants(),
        "homework": store.list_homework(),
        "submissions": store.list_submissions(),
    }
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0


# ---------- Parser ------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    _doc = __doc__ or ""
    p = argparse.ArgumentParser(prog="progress_cli", description=_doc.split("\n\n")[0] if _doc else None)
    p.add_argument("--db", default=str(DEFAULT_DB), help="path to progress.json ledger")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("enroll", help="add a new participant")
    s.add_argument("name")
    s.add_argument("email", nargs="?", default="")
    s.add_argument("--id", default="", help="override the auto-generated participant id")
    s.set_defaults(func=cmd_enroll)

    s = sub.add_parser("participants", help="list all enrolled participants")
    s.set_defaults(func=cmd_list_participants)

    s = sub.add_parser("seed", help="bulk-load a phase's curriculum (idempotent)")
    s.add_argument("phase", choices=("phase-1",))
    s.set_defaults(func=cmd_seed)

    s = sub.add_parser("status", help="dashboard for a single participant")
    s.add_argument("participant")
    s.set_defaults(func=cmd_status)

    s = sub.add_parser("start", help="mark a homework as in_progress")
    s.add_argument("participant"); s.add_argument("homework")
    s.set_defaults(func=cmd_start)

    s = sub.add_parser("submit", help="mark a homework as submitted")
    s.add_argument("participant"); s.add_argument("homework")
    s.add_argument("--evidence", default="")
    s.add_argument("--notes", default="")
    s.set_defaults(func=cmd_submit)

    s = sub.add_parser("approve", help="mark a homework as approved (counts toward completion)")
    s.add_argument("participant"); s.add_argument("homework")
    s.add_argument("--reviewer", default="ned")
    s.add_argument("--notes", default="")
    s.set_defaults(func=cmd_approve)

    s = sub.add_parser("reject", help="mark a homework as rejected (needs another submission)")
    s.add_argument("participant"); s.add_argument("homework")
    s.add_argument("--reviewer", default="ned")
    s.add_argument("--notes", default="")
    s.set_defaults(func=cmd_reject)

    s = sub.add_parser("overdue", help="list all overdue homework across participants")
    s.set_defaults(func=cmd_overdue)

    s = sub.add_parser("dump", help="print the full ledger as JSON")
    s.set_defaults(func=cmd_dump)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    store = ProgressStore(args.db)
    try:
        return args.func(args, store)
    except (ValueError, KeyError) as e:
        print(f"❌ {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

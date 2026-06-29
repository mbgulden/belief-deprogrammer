"""
Progress Tracker + Homework System
==================================

Tracks consultant/bootcamp participants through a multi-phase curriculum
designed to turn them into AI-augmented Human Design consultants. Records:

  - Enrollment (participant, start date, current phase/week)
  - Module / lesson completion
  - Homework submissions (status, payload, evidence, due dates)
  - Milestone events (assessments, certifications, graduations)
  - Stale-task detection (overdue, not-started)

Persistence: a single JSON ledger (data/progress.json) with atomic writes
(via tmp + os.replace). The ledger is human-readable and diff-friendly, which
matches the rest of this project (no DB dependency, no migration story).

Designed for the AI Consultant Bootcamp (GRO-499–GRO-502) but generic
enough to drive any multi-phase coaching program.

Public API (used by CLI + future web layer):
  - Participant, Module, Homework, Submission dataclasses
  - ProgressStore  (CRUD + queries)
  - is_overdue / completion_pct / next_action helpers
"""

from __future__ import annotations

import json
import os
import re
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Iterable


# ---------- Data model --------------------------------------------------------

PHASES = ("phase-1", "phase-2", "phase-3", "phase-4")
STATUSES = ("not_started", "in_progress", "submitted", "approved", "rejected")


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _today_iso() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def _slug(value: str) -> str:
    value = value.strip().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


@dataclass
class Participant:
    """A bootcamp enrollee.

    `id` is stable for the life of the enrollment and used as the foreign key
    on every homework / milestone row. Keep it human-friendly: derived from
    name + year (e.g. "michael-b-2026") but overridable.
    """
    id: str
    name: str
    email: str = ""
    started_at: str = field(default_factory=_utcnow_iso)
    current_phase: str = "phase-1"
    current_week: int = 1
    notes: str = ""

    @classmethod
    def new(cls, name: str, email: str = "", participant_id: str = "") -> "Participant":
        pid = participant_id.strip() or f"{_slug(name)}-{datetime.now(timezone.utc).year}"
        return cls(id=pid, name=name.strip(), email=email.strip())


@dataclass
class Homework:
    """A homework assignment.

    Belongs to a phase + week. Each participant has at most one Submission
    per homework (unique by participant_id + homework_id). `due_days` is the
    number of days after the participant's start date that this is due; 0
    means "no fixed due date" (e.g. self-paced).
    """
    id: str
    phase: str
    week: int
    title: str
    description: str = ""
    deliverable: str = ""        # what they actually hand in (PR, doc, video URL, etc.)
    due_days: int = 7
    weight: int = 1              # 1=normal, 2=checkpoint, 3=capstone

    def __post_init__(self):
        if self.phase not in PHASES:
            raise ValueError(f"phase must be one of {PHASES}, got {self.phase!r}")
        if self.week < 1:
            raise ValueError("week must be >= 1")
        if self.weight not in (1, 2, 3):
            raise ValueError("weight must be 1, 2, or 3")

    def due_date(self, started_at: str) -> str:
        """ISO date string for the homework's due date given an enrollment start."""
        start = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
        return (start + timedelta(days=self.due_days)).date().isoformat()


@dataclass
class Submission:
    """Status of a participant's attempt at a homework assignment."""
    participant_id: str
    homework_id: str
    status: str = "not_started"
    started_at: str = ""
    submitted_at: str = ""
    reviewed_at: str = ""
    reviewer: str = ""
    evidence: str = ""           # URL, PR, or short description
    notes: str = ""

    def __post_init__(self):
        if self.status not in STATUSES:
            raise ValueError(f"status must be one of {STATUSES}, got {self.status!r}")


# ---------- Store -------------------------------------------------------------

class ProgressStore:
    """JSON-file backed progress ledger.

    Schema (top-level keys):
        participants: list[Participant dict]
        homework:     list[Homework dict]
        submissions:  list[Submission dict]
        milestones:   list[dict]    -- audit-trail events

    All writes go through _save() which uses a tmp file + os.replace for
    crash-safety. Reads are cheap (single JSON load) — fine for the expected
    scale (a few hundred participants max).
    """
    SCHEMA_VERSION = 1

    def __init__(self, path: str | os.PathLike):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._save(self._empty())

    # ---- public CRUD ----

    def add_participant(self, name: str, email: str = "", participant_id: str = "") -> Participant:
        p = Participant.new(name, email, participant_id)
        data = self._load()
        if any(x["id"] == p.id for x in data["participants"]):
            raise ValueError(f"participant {p.id!r} already exists")
        data["participants"].append(asdict(p))
        self._save(data)
        return p

    def add_homework(self, hw: Homework) -> Homework:
        data = self._load()
        if any(x["id"] == hw.id for x in data["homework"]):
            raise ValueError(f"homework {hw.id!r} already exists")
        data["homework"].append(asdict(hw))
        self._save(data)
        return hw

    def bulk_add_homework(self, hws: Iterable[Homework]) -> int:
        data = self._load()
        existing = {x["id"] for x in data["homework"]}
        added = 0
        for hw in hws:
            if hw.id not in existing:
                data["homework"].append(asdict(hw))
                added += 1
        self._save(data)
        return added

    def upsert_submission(self, sub: Submission) -> Submission:
        data = self._load()
        for i, existing in enumerate(data["submissions"]):
            if existing["participant_id"] == sub.participant_id and existing["homework_id"] == sub.homework_id:
                data["submissions"][i] = asdict(sub)
                self._save(data)
                return sub
        data["submissions"].append(asdict(sub))
        self._save(data)
        return sub

    def record_milestone(self, participant_id: str, label: str, detail: str = "") -> None:
        data = self._load()
        data["milestones"].append({
            "id": uuid.uuid4().hex[:12],
            "participant_id": participant_id,
            "label": label,
            "detail": detail,
            "at": _utcnow_iso(),
        })
        self._save(data)

    # ---- public queries ----

    def get_participant(self, participant_id: str) -> dict | None:
        return next((p for p in self._load()["participants"] if p["id"] == participant_id), None)

    def list_participants(self) -> list[dict]:
        return list(self._load()["participants"])

    def list_homework(self, phase: str | None = None) -> list[dict]:
        rows = self._load()["homework"]
        return [h for h in rows if phase is None or h["phase"] == phase]

    def list_submissions(self, participant_id: str | None = None) -> list[dict]:
        rows = self._load()["submissions"]
        return [s for s in rows if participant_id is None or s["participant_id"] == participant_id]

    # ---- derived views ----

    def homework_for(self, participant_id: str, phase: str | None = None) -> list[tuple[dict, dict | None]]:
        """Return [(homework, submission_or_None), ...] for a participant, ordered by (phase, week, weight)."""
        data = self._load()
        participant = self.get_participant(participant_id)
        if participant is None:
            raise KeyError(participant_id)
        subs = {s["homework_id"]: s for s in data["submissions"] if s["participant_id"] == participant_id}
        rows: list[tuple[dict, dict | None]] = []
        for hw in data["homework"]:
            if phase is not None and hw["phase"] != phase:
                continue
            rows.append((hw, subs.get(hw["id"])))
        rows.sort(key=lambda r: (r[0]["phase"], r[0]["week"], -r[0]["weight"], r[0]["id"]))
        return rows

    def completion_pct(self, participant_id: str, phase: str | None = None) -> float:
        rows = self.homework_for(participant_id, phase=phase)
        if not rows:
            return 0.0
        earned = sum(h["weight"] for h, s in rows if s and s["status"] == "approved")
        possible = sum(h["weight"] for h, _ in rows)
        return round(earned / possible * 100, 1) if possible else 0.0

    def overdue(self, participant_id: str | None = None, today: str | None = None) -> list[tuple[dict, dict, dict, str]]:
        """Return [(participant, homework, submission, due_date), ...] for items past due that aren't approved."""
        today = today or _today_iso()
        data = self._load()
        participants = {p["id"]: p for p in data["participants"]}
        if participant_id is not None:
            participants = {participant_id: participants[participant_id]} if participant_id in participants else {}
        subs_by_pair = {(s["participant_id"], s["homework_id"]): s for s in data["submissions"]}
        out: list[tuple[dict, dict, dict, str]] = []
        for pid, p in participants.items():
            for hw in data["homework"]:
                sub = subs_by_pair.get((pid, hw["id"]))
                if sub and sub["status"] == "approved":
                    continue
                due = hw["due_days"] and self._due_date(p["started_at"], hw["due_days"]) or ""
                if due and due < today:
                    out.append((p, hw, sub or {"status": "not_started"}, due))
        return out

    def next_action(self, participant_id: str) -> dict | None:
        """Pick the highest-priority not-yet-approved homework the participant should do next.

        Priority order: overdue first, then due-soonest, then by (phase, week, -weight).
        Returns a dict with participant / homework / submission / due_date / reason keys,
        or None if everything in the active phase is approved.
        """
        p = self.get_participant(participant_id)
        if p is None:
            return None
        rows = self.homework_for(participant_id, phase=p["current_phase"])
        today = _today_iso()
        candidates = [(hw, s) for hw, s in rows if not (s and s["status"] == "approved")]
        if not candidates:
            return None

        def _key(pair):
            hw, s = pair
            due = hw["due_days"] and self._due_date(p["started_at"], hw["due_days"]) or "9999-12-31"
            is_overdue = 0 if due < today and not (s and s["status"] == "submitted") else 1
            return (is_overdue, due, hw["phase"], hw["week"], -hw["weight"], hw["id"])

        hw, s = sorted(candidates, key=_key)[0]
        due = hw["due_days"] and self._due_date(p["started_at"], hw["due_days"]) or ""
        return {
            "participant": p,
            "homework": hw,
            "submission": s or {"status": "not_started"},
            "due_date": due,
            "reason": "overdue" if due and due < today else "next up",
        }

    # ---- internals ----

    @staticmethod
    def _due_date(started_at: str, due_days: int) -> str:
        start = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
        return (start + timedelta(days=due_days)).date().isoformat()

    def _empty(self) -> dict:
        return {
            "schema_version": self.SCHEMA_VERSION,
            "participants": [],
            "homework": [],
            "submissions": [],
            "milestones": [],
        }

    def _load(self) -> dict:
        if not self.path.exists():
            return self._empty()
        with self.path.open() as f:
            return json.load(f)

    def _save(self, data: dict) -> None:
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        try:
            with tmp.open("w") as f:
                json.dump(data, f, indent=2, sort_keys=True)
            os.replace(tmp, self.path)
        except BaseException:
            # Don't leak the tmp file on a partial-write crash (disk full,
            # process killed mid-write, os.replace race, etc.)
            try:
                tmp.unlink()
            except FileNotFoundError:
                pass
            raise

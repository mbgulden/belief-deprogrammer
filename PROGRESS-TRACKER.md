# Progress Tracker + Homework System

Part of the **AI Consultant Bootcamp** (GRO-501). Tracks participants through
a multi-phase curriculum of homework assignments, status transitions, and
milestone events. Backed by a single JSON ledger — no DB, no migration story.

## Quick start

```bash
# 1. Seed the Phase 1 curriculum (idempotent — safe to re-run)
python3 -m engine.progress_cli seed phase-1

# 2. Enroll a participant
python3 -m engine.progress_cli enroll "Michael Brave" michael@example.com

# 3. See their dashboard
python3 -m engine.progress_cli status michael-brave-2026

# 4. Move homework through its lifecycle
python3 -m engine.progress_cli start   michael-brave-2026 phase-1-week-1-hw1
python3 -m engine.progress_cli submit  michael-brave-2026 phase-1-week-1-hw1 --evidence https://github.com/x/y/pull/1
python3 -m engine.progress_cli approve michael-brave-2026 phase-1-week-1-hw1 --reviewer fred

# 5. Check who's behind
python3 -m engine.progress_cli overdue
```

## Data model

- **Participant** — one row per enrollee; tracks current phase/week.
- **Homework** — one row per assignment; belongs to `(phase, week)` and has
  a `weight` (1=normal, 2=checkpoint, 3=capstone) and a `due_days` offset
  from the participant's start date.
- **Submission** — one row per `(participant, homework)` pair; status
  walks through `not_started → in_progress → submitted → approved | rejected`.
- **Milestone** — append-only event log (enrolled, homework-approved, etc.).

The default store path is `data/progress.json` relative to the repo root;
override with `--db /path/to/ledger.json`. Writes are atomic
(tmp + `os.replace`) and the tmp file is cleaned up on partial-write
crash.

## How completion is measured

`completion_pct(participant, phase)` is the sum of `weight` for all
**approved** homework in the phase, divided by the total weight of all
homework in the phase, expressed as a percentage. **Submitted** but
**not approved** homework does not count.

## Phase 1 curriculum (seeded by `seed phase-1`)

| ID | Title | Weight | Due |
|---|---|---|---|
| `phase-1-week-1-hw1` | Curate YouTube Expert Library (15-25 videos) | 2 | +7d |
| `phase-1-week-1-hw2` | Design HD-Tailored Self-Coaching Curriculum | 3 | +7d |
| `phase-1-week-2-hw1` | Build Progress Tracker and Homework System | 2 | +14d |
| `phase-1-week-2-hw2` | Execute Week 1 — C-Suite Communication | 3 | +14d |

The Phase 1 curriculum mirrors the GRO-499 → GRO-502 Linear issues so that
each of those issues can be tracked as a homework submission against any
participant. Later phases (2-4) can be added by extending
`PHASE_1_CURRICULUM` and the `seed` subcommand's choices tuple.

## Testing

```bash
python3 -m pytest tests/test_progress_tracker.py -v
```

19 tests cover: slug derivation, dataclass validation, CRUD + duplicate
detection, idempotent bulk seed, submission upsert, completion percentage
weighting, overdue detection skipping approved items, atomic-write crash
recovery, and full CLI lifecycle.

## Files

- `engine/progress_tracker.py` — data model + JSON store + queries
- `engine/progress_cli.py`     — argparse CLI for facilitators
- `tests/test_progress_tracker.py` — unit + CLI integration tests
- `data/progress.json` (created on first run) — the live ledger

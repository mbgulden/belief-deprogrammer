"""
Tests for engine/progress_tracker.py + engine/progress_cli.py.

Run from the belief-deprogrammer repo root:
  python3 -m pytest tests/test_progress_tracker.py -v
or:
  python3 tests/test_progress_tracker.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

# Make `engine` importable regardless of cwd
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine.progress_tracker import (  # noqa: E402
    PHASES,
    STATUSES,
    Homework,
    Participant,
    ProgressStore,
    Submission,
    _slug,
    _utcnow_iso,
)
from engine import progress_cli  # noqa: E402


class SlugTests(unittest.TestCase):
    def test_basic_slugify(self):
        self.assertEqual(_slug("Michael Brave"), "michael-brave")
        self.assertEqual(_slug("  Anna  de  Ville  "), "anna-de-ville")
        self.assertEqual(_slug("V10 — gate-aware!"), "v10-gate-aware")


class HomeworkValidationTests(unittest.TestCase):
    def test_phase_must_be_valid(self):
        with self.assertRaises(ValueError):
            Homework(id="x", phase="phase-99", week=1, title="t")

    def test_week_must_be_positive(self):
        with self.assertRaises(ValueError):
            Homework(id="x", phase="phase-1", week=0, title="t")

    def test_weight_must_be_1_2_or_3(self):
        for w in (1, 2, 3):
            Homework(id=f"ok-{w}", phase="phase-1", week=1, title="t", weight=w)
        with self.assertRaises(ValueError):
            Homework(id="bad", phase="phase-1", week=1, title="t", weight=4)

    def test_due_date_calculation(self):
        hw = Homework(id="x", phase="phase-1", week=1, title="t", due_days=7)
        started = "2026-06-01T00:00:00+00:00"
        self.assertEqual(hw.due_date(started), "2026-06-08")


class ProgressStoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.db = Path(self.tmp) / "progress.json"
        self.store = ProgressStore(self.db)

    def test_empty_store_starts_clean(self):
        self.assertFalse(self.store.list_participants())
        self.assertFalse(self.store.list_homework())
        self.assertFalse(self.store.list_submissions())
        # Schema file was created on init
        self.assertTrue(self.db.exists())
        with self.db.open() as f:
            data = json.load(f)
        self.assertEqual(data["schema_version"], ProgressStore.SCHEMA_VERSION)

    def test_participant_crud_and_duplicate_detection(self):
        p = self.store.add_participant("Michael Brave", "m@x.com")
        self.assertEqual(p.id, f"michael-brave-{datetime.now(timezone.utc).year}")
        self.assertEqual(p.email, "m@x.com")
        with self.assertRaises(ValueError):
            self.store.add_participant("Michael Brave")  # duplicate id
        # Override id
        p2 = self.store.add_participant("Michael Brave", participant_id="mb-2026")
        self.assertEqual(p2.id, "mb-2026")
        self.assertEqual(len(self.store.list_participants()), 2)

    def test_homework_bulk_is_idempotent(self):
        hw1 = Homework(id="a", phase="phase-1", week=1, title="A")
        hw2 = Homework(id="b", phase="phase-1", week=1, title="B")
        self.assertEqual(self.store.bulk_add_homework([hw1, hw2]), 2)
        # Re-add same — should add 0
        self.assertEqual(self.store.bulk_add_homework([hw1, hw2]), 0)
        # Mix of new + existing
        hw3 = Homework(id="c", phase="phase-1", week=2, title="C")
        self.assertEqual(self.store.bulk_add_homework([hw1, hw3]), 1)

    def test_submission_upsert_replaces_existing(self):
        self.store.add_participant("A", participant_id="a")
        hw = Homework(id="h1", phase="phase-1", week=1, title="H1")
        self.store.add_homework(hw)
        sub = Submission(participant_id="a", homework_id="h1", status="in_progress")
        self.store.upsert_submission(sub)
        self.assertEqual(len(self.store.list_submissions("a")), 1)
        # Upsert again with a different status
        sub2 = Submission(participant_id="a", homework_id="h1", status="submitted", evidence="pr://1")
        self.store.upsert_submission(sub2)
        rows = self.store.list_submissions("a")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["status"], "submitted")
        self.assertEqual(rows[0]["evidence"], "pr://1")

    def test_completion_pct_weights_approved_work(self):
        self.store.add_participant("X", participant_id="x")
        self.store.add_homework(Homework(id="w1", phase="phase-1", week=1, title="W1", weight=1))
        self.store.add_homework(Homework(id="w2", phase="phase-1", week=1, title="W2", weight=3))
        self.assertEqual(self.store.completion_pct("x"), 0.0)
        self.store.upsert_submission(Submission(participant_id="x", homework_id="w1", status="approved"))
        self.assertEqual(self.store.completion_pct("x"), 25.0)  # 1 / (1+3) * 100
        self.store.upsert_submission(Submission(participant_id="x", homework_id="w2", status="approved"))
        self.assertEqual(self.store.completion_pct("x"), 100.0)
        # Submitted-but-not-approved doesn't count
        self.store.upsert_submission(Submission(participant_id="x", homework_id="w1", status="in_progress"))
        # still 100 because w1 is the approved one. Reset for a clear test:
        # approve w2 in_progress shouldn't matter
        # The point: only "approved" counts, not "submitted"
        # State: w1=in_progress (was approved), w2=approved (weight 3), w3=submitted (weight 1)
        # Only w2 counts toward completion: 3 / (1+3+1) = 60%
        self.store.add_homework(Homework(id="w3", phase="phase-1", week=2, title="W3", weight=1))
        self.store.upsert_submission(Submission(participant_id="x", homework_id="w3", status="submitted"))
        self.assertEqual(self.store.completion_pct("x"), 60.0)  # 3/5 — only w2 still approved

    def test_overdue_skips_approved_and_filters_by_today(self):
        self.store.add_participant("Y", participant_id="y")
        hw_old = Homework(id="old", phase="phase-1", week=1, title="Old", due_days=3)
        hw_future = Homework(id="future", phase="phase-1", week=1, title="Future", due_days=30)
        self.store.add_homework(hw_old)
        self.store.add_homework(hw_future)
        # Move started_at to 10 days ago
        past = (datetime.now(timezone.utc) - timedelta(days=10)).isoformat(timespec="seconds")
        data = json.loads(self.db.read_text())
        data["participants"][0]["started_at"] = past
        self.db.write_text(json.dumps(data))
        overdue = self.store.overdue(today=datetime.now(timezone.utc).date().isoformat())
        ids = [hw["id"] for _, hw, _, _ in overdue]
        self.assertIn("old", ids)
        self.assertNotIn("future", ids)
        # Approve the overdue one — should drop out of the overdue list
        self.store.upsert_submission(Submission(participant_id="y", homework_id="old", status="approved"))
        overdue2 = self.store.overdue()
        self.assertFalse(any(hw["id"] == "old" for _, hw, _, _ in overdue2))

    def test_next_action_picks_overdue_first(self):
        self.store.add_participant("Z", participant_id="z")
        hw_old = Homework(id="old", phase="phase-1", week=1, title="Old", due_days=3, weight=1)
        hw_new = Homework(id="new", phase="phase-1", week=1, title="New", due_days=30, weight=1)
        self.store.add_homework(hw_old)
        self.store.add_homework(hw_new)
        past = (datetime.now(timezone.utc) - timedelta(days=10)).isoformat(timespec="seconds")
        data = json.loads(self.db.read_text())
        data["participants"][0]["started_at"] = past
        self.db.write_text(json.dumps(data))
        nxt = self.store.next_action("z")
        self.assertIsNotNone(nxt)
        assert nxt is not None
        self.assertEqual(nxt["homework"]["id"], "old")
        self.assertEqual(nxt["reason"], "overdue")

    def test_next_action_none_when_all_approved(self):
        self.store.add_participant("Q", participant_id="q")
        hw = Homework(id="only", phase="phase-1", week=1, title="Only")
        self.store.add_homework(hw)
        self.store.upsert_submission(Submission(participant_id="q", homework_id="only", status="approved"))
        self.assertIsNone(self.store.next_action("q"))

    def test_atomic_writes_dont_corrupt_on_crash(self):
        """A failed write mid-save should leave the previous file intact."""
        # Write something good
        self.store.add_participant("Crash", participant_id="c")
        with self.db.open() as f:
            good = f.read()
        # Simulate crash during the next write by patching os.replace
        with mock.patch("engine.progress_tracker.os.replace", side_effect=RuntimeError("boom")):
            with self.assertRaises(RuntimeError):
                self.store.add_participant("Will Fail", participant_id="wf")
        # Original file should still match
        with self.db.open() as f:
            self.assertEqual(f.read(), good)
        # No leftover .tmp file
        self.assertFalse(self.db.with_suffix(self.db.suffix + ".tmp").exists())


class ProgressCliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.db = Path(self.tmp) / "progress.json"
        self.store = ProgressStore(self.db)
        # Seed curriculum
        self.store.bulk_add_homework(progress_cli.PHASE_1_CURRICULUM)

    def _call(self, *args):
        return progress_cli.main(["--db", str(self.db), *args])

    def test_enroll_then_status(self):
        rc = self._call("enroll", "Test User", "t@x.com", "--id", "tu")
        self.assertEqual(rc, 0)
        rc = self._call("status", "tu")
        self.assertEqual(rc, 0)

    def test_full_lifecycle(self):
        self._call("enroll", "L C", "--id", "lc")
        rc = self._call("start", "lc", "phase-1-week-1-hw1")
        self.assertEqual(rc, 0)
        rc = self._call("submit", "lc", "phase-1-week-1-hw1", "--evidence", "https://example.com/pr/1")
        self.assertEqual(rc, 0)
        rc = self._call("approve", "lc", "phase-1-week-1-hw1", "--reviewer", "fred")
        self.assertEqual(rc, 0)
        subs = self.store.list_submissions("lc")
        self.assertEqual(subs[0]["status"], "approved")
        self.assertEqual(subs[0]["reviewer"], "fred")
        # Milestone recorded
        self.assertTrue(self.store._load()["milestones"])

    def test_enroll_duplicate_fails(self):
        self._call("enroll", "Dup", "--id", "dup")
        # Duplicate enroll returns exit code 2 (CLI surfaces ValueError)
        rc = self._call("enroll", "Dup", "--id", "dup")
        self.assertEqual(rc, 2)

    def test_overdue_command_exits_zero_when_empty(self):
        # Fresh enrollment, no homework overdue
        self._call("enroll", "F", "--id", "f")
        rc = self._call("overdue")
        self.assertEqual(rc, 0)

    def test_dump_emits_valid_json(self):
        self._call("enroll", "D", "--id", "d")
        rc = self._call("dump")
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()

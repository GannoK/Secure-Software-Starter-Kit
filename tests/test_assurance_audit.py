from __future__ import annotations

import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("assurance_audit", ROOT / "tools" / "assurance_audit.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class AssuranceAuditTests(unittest.TestCase):
    def test_full_sha(self):
        self.assertTrue(MODULE.is_full_sha("f" * 40))
        self.assertFalse(MODULE.is_full_sha("v4"))

    def test_mutable_action_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "workflow.yml"
            path.write_text(
                "permissions: read-all\nsteps:\n"
                "  - uses: actions/checkout@v4\n"
                "    with:\n"
                "      persist-credentials: false\n",
                encoding="utf-8",
            )
            self.assertTrue(any("unpinned action" in item for item in MODULE.workflow_findings(path)))

    def test_expired_exception(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "exception.md"
            path.write_text("Review or expiration date: 2026-01-01\n", encoding="utf-8")
            self.assertTrue(MODULE.expired_exception(path, today=date(2026, 9, 11)))

    def test_future_exception(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "exception.md"
            path.write_text("Review or expiration date: 2027-01-01\n", encoding="utf-8")
            self.assertFalse(MODULE.expired_exception(path, today=date(2026, 9, 11)))


if __name__ == "__main__":
    unittest.main()

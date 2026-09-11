#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT_STATES = {"PASS", "FAIL", "MANUAL", "N/A", "UNKNOWN", "WAIVED"}
SHA40 = re.compile(r"^[0-9a-f]{40}$")
USES = re.compile(r"^\s*-?\s*uses:\s*([^@\s]+)@([^\s#]+)", re.MULTILINE)


def is_full_sha(ref: str) -> bool:
    return bool(SHA40.fullmatch(ref))


def workflow_findings(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    try:
        display = path.relative_to(ROOT).as_posix()
    except ValueError:
        display = path.as_posix()
    findings: list[str] = []
    for action, ref in USES.findall(text):
        if action.startswith("./"):
            continue
        if not is_full_sha(ref):
            findings.append(f"{display}: unpinned action {action}@{ref}")
    if "permissions:" not in text:
        findings.append(f"{display}: missing explicit permissions")
    if "actions/checkout@" in text and "persist-credentials: false" not in text:
        findings.append(f"{display}: checkout must disable credential persistence")
    return findings


def expired_exception(path: Path, today: date | None = None) -> bool:
    today = today or date.today()
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"Review or expiration date:\s*(\d{4}-\d{2}-\d{2})", text)
    if not match:
        return False
    try:
        return datetime.strptime(match.group(1), "%Y-%m-%d").date() < today
    except ValueError:
        return True


def audit() -> tuple[list[str], list[str]]:
    failures: list[str] = []
    manual: list[str] = []

    required = [
        "ASSURANCE.json",
        "GOVERNANCE.md",
        "MAINTAINERS.md",
        ".github/CODEOWNERS",
        "SECURITY.md",
        "09_REFERENCE/05_STANDARDS_CROSSWALK.md",
        "05_SECURITY/08_SLSA_PROVENANCE_PROFILE.md",
        "05_SECURITY/09_SECURE_DEFAULTS_REVIEW.md",
        "05_SECURITY/10_SECURITY_REGRESSION_TAXONOMY.md",
        "06_TEMPLATES/10_SECURITY_CONTROL_EVIDENCE_TEMPLATE.json",
        "06_TEMPLATES/11_SECURITY_EXCEPTION_TEMPLATE.md",
    ]
    for rel in required:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required assurance artifact: {rel}")

    try:
        manifest = json.loads((ROOT / "ASSURANCE.json").read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"ASSURANCE.json invalid: {exc}")
        manifest = {}

    if set(manifest.get("result_states", [])) != RESULT_STATES:
        failures.append(f"ASSURANCE.json result_states must equal {sorted(RESULT_STATES)}")

    workflows = ROOT / ".github" / "workflows"
    if workflows.is_dir():
        for path in sorted(workflows.glob("*.y*ml")):
            failures.extend(workflow_findings(path))

    exceptions = ROOT / "assurance" / "exceptions"
    if exceptions.is_dir():
        for path in sorted(exceptions.glob("*.md")):
            if expired_exception(path):
                failures.append(f"expired security exception: {path.relative_to(ROOT)}")

    manual.extend([
        "threat_model_quality",
        "cryptographic_design_review",
        "security_test_coverage",
        "two_person_review_where_required",
        "vulnerability_response_performance",
    ])
    return failures, manual


def main() -> int:
    failures, manual = audit()
    for item in manual:
        print(f"MANUAL: {item}")
    for item in failures:
        print(f"FAIL: {item}")
    if failures:
        print(f"ASSURANCE_AUDIT=FAIL failures={len(failures)} manual={len(manual)}")
        return 1
    print(f"ASSURANCE_AUDIT=PASS failures=0 manual={len(manual)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

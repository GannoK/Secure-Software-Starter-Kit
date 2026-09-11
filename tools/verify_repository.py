#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from assurance_audit import audit as assurance_audit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "OPEN_THIS_FIRST.md", "LICENSE", "ATTRIBUTION.md",
    "SECURITY.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "GOVERNANCE.md", "MAINTAINERS.md", "ASSURANCE.json",
    ".github/CODEOWNERS",
    "PACK_METADATA.json", "PUBLIC_RELEASE_READINESS.md", "MANIFEST_SHA256.txt",
    "00_QUICK_START/QUICK_START_ONE_PAGE.md",
    "01_BEGINNER_GUIDE/02_FIVE_MINUTE_SETUP.md",
    "05_SECURITY/01_MINIMUM_SECURE_SOFTWARE_BASELINE.md",
    "05_SECURITY/08_SLSA_PROVENANCE_PROFILE.md",
    "05_SECURITY/09_SECURE_DEFAULTS_REVIEW.md",
    "05_SECURITY/10_SECURITY_REGRESSION_TAXONOMY.md",
    "09_REFERENCE/05_STANDARDS_CROSSWALK.md",
    "06_TEMPLATES/10_SECURITY_CONTROL_EVIDENCE_TEMPLATE.json",
    "06_TEMPLATES/11_SECURITY_EXCEPTION_TEMPLATE.md",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        fail(f"required file missing: {rel}")

try:
    meta = json.loads((ROOT / "PACK_METADATA.json").read_text(encoding="utf-8"))
except Exception as exc:
    fail(f"PACK_METADATA.json is invalid: {exc}")

if meta.get("license") != "CC-BY-4.0":
    fail("PACK_METADATA.json license must be CC-BY-4.0")
if meta.get("status") != "public-release":
    fail("PACK_METADATA.json status must be public-release")

manifest = ROOT / "MANIFEST_SHA256.txt"
seen = set()
for lineno, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
    if not raw.strip():
        continue
    match = re.fullmatch(r"([0-9a-f]{64})  (.+)", raw)
    if not match:
        fail(f"invalid manifest line {lineno}")
    expected, rel = match.groups()
    path = ROOT / rel
    if not path.is_file():
        fail(f"manifest file missing: {rel}")
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        fail(f"checksum mismatch: {rel}")
    seen.add(rel)

link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8", errors="replace")
    for match in link_pattern.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = target.split("#", 1)[0]
        if target_path and not (md.parent / target_path).resolve().exists():
            fail(f"broken local Markdown link in {md.relative_to(ROOT)}: {target}")

expected_files = {
    p.relative_to(ROOT).as_posix()
    for p in ROOT.rglob("*")
    if p.is_file()
    and p.name != "MANIFEST_SHA256.txt"
    and ".git" not in p.parts
    and "__pycache__" not in p.parts
}
if seen != expected_files:
    missing = sorted(expected_files - seen)
    stale = sorted(seen - expected_files)
    if missing:
        print("Manifest missing entries:")
        for rel in missing:
            print(f"  {rel}")
    if stale:
        print("Manifest has stale entries:")
        for rel in stale:
            print(f"  {rel}")
    fail("manifest set does not exactly match repository files")

assurance_failures, manual_controls = assurance_audit()
if assurance_failures:
    for item in assurance_failures:
        print(f"ASSURANCE_FAIL: {item}")
    fail(f"assurance policy failures: {len(assurance_failures)}")

print(
    f"REPOSITORY_VERIFY=PASS files={len(expected_files)} "
    f"manual_controls={len(manual_controls)}"
)

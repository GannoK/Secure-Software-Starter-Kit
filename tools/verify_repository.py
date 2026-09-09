#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "OPEN_THIS_FIRST.md", "LICENSE", "COPYRIGHT.md",
    "LICENSE_HISTORY.md", "LICENSE_DECISION.md", "THIRD_PARTY_NOTICES.md",
    "ATTRIBUTION.md", "SECURITY.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "PACK_METADATA.json", "PUBLIC_RELEASE_READINESS.md", "MANIFEST_SHA256.txt",
    "LEGAL/IP_OWNERSHIP_POLICY.md", "LEGAL/CONTRIBUTOR_POLICY.md",
    "LEGAL/AI_ASSISTED_AUTHORSHIP_POLICY.md",
    "00_QUICK_START/QUICK_START_ONE_PAGE.md",
    "01_BEGINNER_GUIDE/02_FIVE_MINUTE_SETUP.md",
    "05_SECURITY/01_MINIMUM_SECURE_SOFTWARE_BASELINE.md",
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

if meta.get("license") != "Proprietary-All-Rights-Reserved":
    fail("PACK_METADATA.json license must be Proprietary-All-Rights-Reserved")
if meta.get("status") != "proprietary-baseline":
    fail("PACK_METADATA.json status must be proprietary-baseline")
if meta.get("version") != "1.2.0":
    fail("PACK_METADATA.json version must be 1.2.0")

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
    raise SystemExit(1)

print(f"REPOSITORY_VERIFY=PASS files={len(expected_files)}")

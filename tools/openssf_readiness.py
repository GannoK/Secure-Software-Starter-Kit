#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = [
    ("security_policy", "SECURITY.md", "PASS"),
    ("contributing", "CONTRIBUTING.md", "PASS"),
    ("code_of_conduct", "CODE_OF_CONDUCT.md", "PASS"),
    ("governance", "GOVERNANCE.md", "PASS"),
    ("maintainers", "MAINTAINERS.md", "PASS"),
    ("codeowners", ".github/CODEOWNERS", "PASS"),
    ("scorecard_workflow", ".github/workflows/scorecard.yml", "PASS"),
    ("codeql_workflow", ".github/workflows/codeql.yml", "PASS"),
    ("dependency_updates", ".github/dependabot.yml", "PASS"),
    ("threat_model_guidance", "05_SECURITY/02_THREAT_MODEL_FOR_NORMAL_PEOPLE.md", "PASS"),
    ("supply_chain_guidance", "05_SECURITY/04_DEPENDENCIES_SBOM_AND_SUPPLY_CHAIN.md", "PASS"),
    ("release_gate_guidance", "05_SECURITY/06_PRODUCTION_SECURITY_GATES.md", "PASS"),
    ("slsa_profile", "05_SECURITY/08_SLSA_PROVENANCE_PROFILE.md", "PASS"),
]

MANUAL = [
    "bus_factor",
    "review_discipline",
    "vulnerability_response_sla_performance",
    "test_coverage_thresholds",
    "cryptographic_design_quality",
]


def main() -> int:
    failed = 0
    passed = 0
    for control, rel, _ in CHECKS:
        if (ROOT / rel).is_file():
            passed += 1
            print(f"PASS: {control} -> {rel}")
        else:
            failed += 1
            print(f"FAIL: {control} -> missing {rel}")
    for control in MANUAL:
        print(f"MANUAL: {control}")
    print(f"OPENSSF_READINESS passed={passed} failed={failed} manual={len(MANUAL)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

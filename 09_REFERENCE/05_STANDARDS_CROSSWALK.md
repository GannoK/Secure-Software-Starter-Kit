# Standards Crosswalk

This crosswalk is an implementation aid, not a certification claim. A mapped document or control does not by itself prove conformance.

| External baseline | Starter Kit coverage | Verification model |
|---|---|---|
| OpenSSF Best Practices | governance, security reporting, quality, change control, dependency/supply-chain guidance, release practices | `tools/openssf_readiness.py` plus manual review |
| OpenSSF Scorecard | pinned dependencies, token permissions, security policy, code review expectations, dependency update tooling, SAST | scheduled Scorecard workflow |
| NIST SSDF SP 800-218 v1.1 | secure development lifecycle, provenance, change control, vulnerability response, software integrity | mapped guidance and project evidence |
| SLSA 1.2 | build/source provenance concepts and tagged-release attestations | `05_SECURITY/08_SLSA_PROVENANCE_PROFILE.md` and release workflow |
| CISA Secure by Design | secure defaults, customer security outcomes, reducing unsafe-by-default choices | secure-defaults review |
| OWASP guidance | threat modeling, input and dependency risk, secrets, AI/RAG security | project-specific application required |

## Interpretation

Use the states `PASS`, `FAIL`, `MANUAL`, `N/A`, `UNKNOWN`, and `WAIVED`.

- `PASS` requires evidence.
- `MANUAL` means automation cannot make the decision responsibly.
- `UNKNOWN` is unresolved and never counts as PASS.
- `WAIVED` requires an explicit exception record and review/expiration date.
- External certification or badge programs remain authoritative for their own conformance claims.

Standards evolve. Record the version used during an assessment and re-check mappings when a baseline changes.

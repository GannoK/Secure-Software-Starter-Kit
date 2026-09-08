# HIGH ASSURANCE profile

Purpose: systems where compromise, incorrect behavior, or unauthorized change could cause severe harm.

Includes **all PRODUCTION controls**, plus stronger assurance.

## Governance and traceability
- [ ] Requirements, threat model, architecture, decisions, tests, and release evidence are versioned.
- [ ] Every high-impact requirement maps to verification evidence.
- [ ] Exceptions have an owner, rationale, expiration/review date, and compensating controls.
- [ ] Security assumptions are explicit and tested where possible.
- [ ] Mutable operational state is never silently inferred from documentation.

## Independent verification
- [ ] Critical controls receive review independent of the implementer.
- [ ] AI-generated security-sensitive code is independently reviewed.
- [ ] High-risk changes require multi-party approval appropriate to the organization.
- [ ] Penetration testing or equivalent adversarial assessment is performed where appropriate.
- [ ] Critical threat mitigations have negative/adversarial tests.

## Privilege and isolation
- [ ] Administrative duties use separate identities/roles where practical.
- [ ] Build/release credentials are tightly scoped and protected.
- [ ] Production access is minimized, logged, and reviewed.
- [ ] Development/test and production boundaries are explicit.
- [ ] High-impact AI agents are sandboxed or otherwise strongly constrained.
- [ ] No model output directly obtains unrestricted privileged execution.

## Supply chain
- [ ] Source/release provenance is strongly authenticated.
- [ ] Reproducibility or equivalent independent build verification is considered.
- [ ] SBOM and vulnerability response are operational processes, not one-time files.
- [ ] Dependencies and build tooling have explicit trust/risk review.
- [ ] Release artifacts are signed/authenticated where feasible.
- [ ] Protected branches/tags and release authority are tightly controlled.

## Resilience and recovery
- [ ] Backups are isolated appropriately and restoration is exercised.
- [ ] Disaster recovery objectives are defined.
- [ ] Incident-response procedures are tested.
- [ ] Audit/security logs have appropriate integrity and retention.
- [ ] Rollback and recovery do not depend on the compromised component alone.

## Assurance rule

"High assurance" cannot be established by a prompt, scanner score, or checklist alone. Use qualified domain, security, compliance, safety, privacy, and legal expertise appropriate to the consequences and jurisdiction.

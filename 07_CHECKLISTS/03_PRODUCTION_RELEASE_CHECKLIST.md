# Production release checklist

## Scope
- [ ] Exact release version/commit identified.
- [ ] Requirements for this release are accepted.
- [ ] No accidental unrelated changes.

## Functional verification
- [ ] Unit tests pass.
- [ ] Integration tests pass.
- [ ] End-to-end critical paths pass.
- [ ] Negative/error paths tested.
- [ ] Regression tests pass.

## Security
- [ ] Authentication verified.
- [ ] Authorization negative tests pass.
- [ ] Input validation reviewed/tested.
- [ ] Secret scan passed.
- [ ] SAST findings triaged.
- [ ] Dependency/SCA findings triaged.
- [ ] Threat model reviewed for architectural changes.
- [ ] Secure production configuration verified.
- [ ] Logs avoid secrets/sensitive data.

## Supply chain
- [ ] Dependencies locked/pinned where practical.
- [ ] SBOM generated where appropriate.
- [ ] Build/source provenance recorded.
- [ ] Release artifact authenticity/signing considered.

## Operations
- [ ] Backup verified where relevant.
- [ ] Rollback documented.
- [ ] Monitoring/logging ready.
- [ ] Failure/health checks defined.
- [ ] Patch/vulnerability response path exists.

## Decision
- [ ] RELEASE READY
- [ ] READY WITH EXPLICIT ACCEPTED RISKS
- [ ] NOT READY

# PRODUCTION profile

Purpose: baseline for software used by real people or handling meaningful real data.

Includes **all STARTER controls**, plus:

## Requirements and architecture
- [ ] Security and privacy requirements are testable.
- [ ] Trust boundaries and data flows are documented.
- [ ] Internet-exposed surfaces are explicitly inventoried.
- [ ] Failure behavior and recovery are designed.
- [ ] Architectural security changes receive explicit review.

## Identity and authorization
- [ ] Authentication is production-appropriate.
- [ ] Authorization is enforced server-side.
- [ ] Cross-user/cross-tenant negative tests exist.
- [ ] Administrator operations are separately protected.
- [ ] MFA is enabled for important operator/developer accounts where supported.

## Engineering pipeline
- [ ] Protected trusted branch is configured where practical.
- [ ] CI runs functional tests.
- [ ] Secret scanning runs.
- [ ] SAST runs and findings are triaged.
- [ ] Dependency/SCA scanning runs and findings are triaged.
- [ ] Security-relevant regression tests are retained.

## Dependencies and supply chain
- [ ] Dependency versions are controlled.
- [ ] An SBOM is generated for release artifacts where practical.
- [ ] Exact release source revision is recorded.
- [ ] Build provenance/source-to-artifact traceability is recorded.
- [ ] Release artifact signing/authentication is considered for the ecosystem.

## Operations
- [ ] Production secrets use an appropriate protected mechanism.
- [ ] TLS/HTTPS is used for networked production services.
- [ ] Logs/metrics support diagnosis without leaking sensitive data.
- [ ] Backups and restoration are tested when data matters.
- [ ] Rollback exists and is understood.
- [ ] Monitoring/health checks exist.
- [ ] Vulnerability intake and patch/update process exist.
- [ ] Production changes have explicit approval and post-change verification.

## AI/RAG/agents, if applicable
- [ ] Retrieval permissions match data permissions.
- [ ] Cross-user knowledge leakage is tested.
- [ ] Prompt injection is an explicit threat.
- [ ] Tools use least-privilege credentials.
- [ ] Consequential agent actions require approval.
- [ ] Generated output is validated before interpreters/tools consume it.

## Release rule

Unresolved security blockers mean **NOT READY**. A working demo is not a production security argument.

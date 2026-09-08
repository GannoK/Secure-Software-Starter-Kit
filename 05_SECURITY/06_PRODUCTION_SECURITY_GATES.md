# Production security gates

Before software with real users or sensitive data goes live, require explicit answers.

## Gate A — Identity
- Authentication design reviewed.
- Authorization is server-side and tested.
- Admin functions are separated/protected.
- MFA enabled for important operator accounts where supported.

## Gate B — Data
- Sensitive data inventory exists.
- Data retention is intentional.
- Secrets are externalized.
- Logs avoid secrets/private content.
- Backups/recovery exist when data matters.

## Gate C — Application
- Inputs validated.
- Injection-sensitive operations use safe APIs.
- Errors fail safely.
- Rate/resource limits considered.
- Security headers/configuration considered for web apps.
- No debug/development exposure in production.

## Gate D — Dependencies
- Dependency inventory known.
- Critical/high known vulnerabilities reviewed.
- Lockfiles/pinning used where practical.
- SBOM generated for production releases where practical.
- Unfamiliar or AI-suggested packages verified.

## Gate E — Verification
- Functional tests pass.
- Authorization negative tests pass.
- Secret scan passes.
- SAST passes or findings triaged.
- SCA/dependency scan passes or findings triaged.
- Relevant manual security review completed.

## Gate F — Release
- Exact release source revision recorded.
- Configuration/migrations documented.
- Rollback plan exists.
- Backup verified where relevant.
- Monitoring/logging exists.
- Known accepted risks are explicitly recorded.

Unresolved blockers mean **NOT READY**, even if the feature appears to work.

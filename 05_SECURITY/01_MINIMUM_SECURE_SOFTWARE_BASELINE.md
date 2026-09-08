# Minimum secure software baseline

These are practical minimums, not a claim of formal compliance.

## Identity and access

- Require authentication for private resources.
- Enforce authorization on the server, not only in the UI.
- Default to least privilege.
- Use MFA for important developer/repository/cloud accounts where available.
- Separate ordinary-user and administrator privileges.
- Test that one user cannot access another user's protected resources.

## Secrets

- Never hard-code production secrets.
- Do not commit `.env` files containing real secrets.
- Use a secret manager or protected environment variables.
- Rotate exposed secrets.
- Limit every credential's permissions and lifetime where possible.
- Keep secrets out of logs.

## Input and output

- Treat user, network, file, API, database, and retrieved AI content as untrusted.
- Validate inputs using allowlists/types/ranges where practical.
- Use parameterized database queries.
- Avoid building shell commands from untrusted strings.
- Encode output for its destination context.
- Validate AI-generated output before passing it to interpreters or privileged tools.

## Dependencies

- Use official package registries/sources.
- Verify unfamiliar package names before installing.
- Lock/pin dependencies where the ecosystem supports it.
- Keep a dependency update process.
- Run software-composition/dependency vulnerability scanning.
- Remove unused dependencies.

## Application design

- Use secure defaults.
- Minimize exposed services and ports.
- Fail safely.
- Rate-limit abuse-sensitive endpoints.
- Apply resource limits/timeouts.
- Protect state-changing requests appropriately.
- Do not invent custom cryptography.
- Use maintained frameworks/libraries for security-sensitive primitives.

## Engineering controls

- Version control.
- Protected trusted branch where practical.
- Automated tests.
- Secret scanning.
- Static analysis.
- Dependency/SCA scanning.
- Security-relevant negative tests.
- Review before production release.

## Operations

- HTTPS/TLS for networked production applications.
- Useful security logging without sensitive-data leakage.
- Backups for important state.
- Tested recovery.
- Patch/vulnerability process.
- Incident contact/process.
- Rollback plan.

## Supply chain

For production software, aim to know:
- exactly what source revision was released;
- exactly what dependencies were included;
- how the artifact was built;
- whether build provenance is available;
- whether release artifacts can be authenticated.

Use an SBOM format such as SPDX or CycloneDX when appropriate.

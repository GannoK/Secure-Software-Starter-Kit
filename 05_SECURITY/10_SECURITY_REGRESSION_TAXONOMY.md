# Security Regression Taxonomy

Use stable categories so security fixes become reusable engineering evidence.

- `AUTHORITY_BOUNDARY` — actor or component can exceed intended authority.
- `AUTHENTICATION` — identity proof or session handling failure.
- `AUTHORIZATION` — incorrect access decision.
- `INPUT_VALIDATION` — unsafe handling of untrusted input.
- `SECRETS` — credential or secret exposure/handling defect.
- `DEPENDENCY` — vulnerable, untrusted, stale, or policy-incompatible dependency.
- `SUPPLY_CHAIN` — build, CI, provenance, signing, or artifact-integrity defect.
- `PRIVILEGE` — unnecessary or uncontrolled privilege.
- `CRYPTO` — cryptographic design, implementation, key, or parameter defect.
- `NETWORK_EXPOSURE` — unintended listener, route, remote access, or insecure transport.
- `PROMPT_INJECTION` — untrusted content changes AI/agent behavior outside intended authority.
- `DATA_PROVENANCE` — origin, integrity, version, or lineage cannot be established.
- `LOGGING_PRIVACY` — logging leaks sensitive data or prevents accountable investigation.
- `RECOVERY_ROLLBACK` — remediation cannot be safely reversed or recovered.
- `SECURE_DEFAULTS` — safe behavior depends on users discovering optional hardening.

Where practical, a confirmed security defect should add a regression test or machine-verifiable control before closure.

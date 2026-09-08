# Security Profile

## Assurance profile

Choose one:

- **STARTER** - learning/local prototype, preferably fake/test data.
- **PRODUCTION** - real users, internet exposure, or meaningful real data.
- **HIGH ASSURANCE** - high-impact, regulated, safety/security-critical, or severe-consequence systems.

Selected profile: [STARTER / PRODUCTION / HIGH ASSURANCE]

See `05_SECURITY/PROFILES/` in the starter pack for the minimum control set.


## Assets to protect

- user accounts;
- credentials/tokens;
- private data;
- database;
- source code;
- signing keys;
- infrastructure;
- logs;
- backups;
- AI/RAG knowledge sources;
- [other].

## Threat actors

- unauthenticated internet user;
- ordinary authenticated user;
- compromised account;
- malicious dependency;
- malicious uploaded/retrieved document;
- compromised third-party service;
- insider;
- automated bot;
- [other].

## Security requirements

- Authentication:
- Authorization:
- Secrets storage:
- Encryption in transit:
- Encryption at rest:
- Input validation:
- Output encoding:
- Logging:
- Backups:
- Dependency scanning:
- Secret scanning:
- SAST:
- DAST where applicable:
- SBOM:
- Release provenance:
- Vulnerability reporting:
- Patch/update process:

## AI/RAG boundaries

- Retrieved content is untrusted input.
- Retrieved text may contain malicious instructions.
- Knowledge access must respect user/data permissions.
- AI output must be validated before it reaches interpreters, shells, databases, HTML renderers, or privileged tools.
- Tool permissions should be least-privilege and scoped.
- High-impact actions require explicit human approval.

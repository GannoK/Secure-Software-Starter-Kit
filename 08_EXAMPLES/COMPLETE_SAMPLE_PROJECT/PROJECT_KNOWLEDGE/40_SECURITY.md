# Security Profile

Current development profile: STARTER
Required before public launch: PRODUCTION

## Assets

- account credentials;
- email addresses;
- borrowing history;
- private contact information;
- database;
- deployment secrets.

## Primary threats

### THREAT-001 - Broken object-level authorization
User A changes an object ID to edit User B's listing.

Mitigation:
server verifies authenticated user owns the exact listing.

Verification:
automated two-user negative test expects denial and no DB change.

### THREAT-002 - Injection
Attacker submits crafted input.

Mitigation:
typed validation plus parameterized ORM/database APIs; no string-built SQL.

### THREAT-003 - Credential leakage
Secrets enter source control or logs.

Mitigation:
environment/secret store, `.gitignore`, secret scan, log review.

### THREAT-004 - Privacy leak
Exact address or private contact information appears in public listing/API.

Mitigation:
public response schema excludes those fields; response-shape tests.

### THREAT-005 - Malicious dependency
Typosquatted or compromised package enters build.

Mitigation:
verify package identity/source, lock versions, dependency scanning.

## Required production checks

- authentication review;
- authorization negative tests;
- secret scan;
- SAST;
- dependency/SCA scan;
- HTTPS;
- backup/restore check;
- SBOM;
- release revision/provenance record.

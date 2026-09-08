# Safe software lifecycle for AI-assisted projects

Use this lifecycle even for small projects. The depth changes; the principles do not.

## Gate 0 — Idea

Answer:
- What problem are we solving?
- Who is it for?
- What would success look like?
- What should this version explicitly not do?

**Exit:** clear project brief.

## Gate 1 — Requirements

Write testable requirements.

Bad:
> The login should be secure.

Better:
> A user must authenticate before viewing private records, and one user must not be able to read another user's records.

**Exit:** requirements and acceptance tests.

## Gate 2 — Security profile and threat model

Identify:
- valuable assets;
- trust boundaries;
- attackers/abuse cases;
- sensitive data;
- highest-impact failures.

**Exit:** initial security requirements.

## Gate 3 — Architecture

Decide components, interfaces, data flow, storage, external dependencies, and failure behavior.

Prefer mature components for commodity problems. Build custom security-critical mechanisms only when you have a strong reason and appropriate expertise.

**Exit:** architecture that can satisfy requirements and security constraints.

## Gate 4 — Small implementation slice

Build the smallest meaningful vertical slice.

Example:
- database schema;
- one API endpoint;
- one UI path;
- authentication boundary;
- tests.

Do not implement ten unrelated features simultaneously.

**Exit:** code exists and can be tested.

## Gate 5 — Verification

Use evidence:
- unit tests;
- integration tests;
- end-to-end tests;
- negative tests;
- authorization tests;
- static analysis;
- dependency scan;
- secret scan.

**Exit:** explicit PASS/FAIL/INCOMPLETE.

## Gate 6 — Security and supply-chain review

Before real users:
- review threat model;
- review OWASP risks applicable to the product;
- generate an SBOM;
- verify dependencies;
- review build/release provenance;
- ensure secrets are not in source/history;
- verify secure defaults;
- verify logging does not leak sensitive data.

**Exit:** no unresolved release blockers.

## Gate 7 — Release preparation

Record:
- exact version/commit;
- configuration;
- migrations;
- backup;
- rollback;
- release notes;
- known accepted risks.

**Exit:** reproducible release candidate.

## Gate 8 — Controlled deployment

Prefer staged deployment when possible.

Verify real health after deployment. "The command completed" does not necessarily mean the application works.

**Exit:** production acceptance checks pass.

## Gate 9 — Operate and maintain

Security continues after release:
- monitor;
- patch dependencies;
- triage vulnerabilities;
- test backups;
- update threat model when architecture changes;
- preserve incident evidence;
- maintain a vulnerability-reporting path.

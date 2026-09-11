# Governance

This repository is a public secure-software engineering starter kit. Its security and assurance guidance should remain technically defensible, evidence-based, beginner-usable, and explicit about what automation can and cannot prove.

## Decision model

- Maintainers may merge routine corrections and non-material improvements after verification.
- Changes to assurance profiles, security baselines, threat-model guidance, supply-chain requirements, release gates, licensing, or security-reporting policy require explicit maintainer review.
- Security controls that require human judgment must remain `MANUAL`, `UNKNOWN`, or `WAIVED` until evidence justifies another state.
- Material changes should document rationale, compatibility impact, security impact, and migration expectations.

## Release governance

A public release should pass automated repository and assurance checks, preserve checksum integrity, identify unresolved controls, and produce release evidence tied to a specific commit.

## Exceptions

Security exceptions must be explicit, scoped, justified, time-bounded or review-bounded, and accompanied by compensating controls where practical. Silent exceptions are not acceptable.

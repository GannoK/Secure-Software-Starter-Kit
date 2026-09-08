# Choose your assurance profile

You do not need every security control on day one. You **do** need a level of rigor appropriate to what your software can affect.

This pack provides three profiles.

## STARTER

Use when:
- learning;
- prototyping;
- building locally;
- using fake/test data;
- no real users depend on the software.

You still use source control, protect secrets, validate inputs, test changes, and keep backups for anything you care about.

Start with:
`05_SECURITY/PROFILES/01_STARTER_PROFILE.md`

## PRODUCTION

Use when:
- real users use the software;
- the application is internet-facing;
- real private data is stored;
- downtime or compromise would matter;
- you are distributing software to other people.

This adds stronger review, CI security checks, authorization tests, SBOM/provenance expectations, monitoring, recovery, and release gates.

Use:
`05_SECURITY/PROFILES/02_PRODUCTION_PROFILE.md`

## HIGH ASSURANCE

Use when failure could cause major harm or when the software handles high-impact domains such as:
- financial assets;
- healthcare or highly sensitive personal data;
- identity/access infrastructure;
- safety-critical systems;
- regulated environments;
- critical infrastructure;
- privileged enterprise administration;
- signing/release infrastructure.

This profile requires much stronger independence, traceability, review, isolation, evidence, and professional expertise.

Use:
`05_SECURITY/PROFILES/03_HIGH_ASSURANCE_PROFILE.md`

## Important

Profiles are **minimum starting points**, not certificates.

Moving from STARTER to PRODUCTION or HIGH ASSURANCE is not just "turning on more scanners." Architecture, authorization, operations, recovery, supply chain, and human review all become more important.

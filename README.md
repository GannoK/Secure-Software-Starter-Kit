# Secure Software Starter Kit

A beginner-friendly framework for designing, building, testing, reviewing, and documenting secure software with AI assistance and modern engineering practices.

**Current release:** Secure Software Starter Kit v1.1
**Start here:** [`OPEN_THIS_FIRST.md`](OPEN_THIS_FIRST.md)

This repository is intended for people who want the leverage of AI-assisted software development without treating an LLM as an unquestionable authority. No programming experience is required to begin.

## Security is not a magic phrase

Building secure software is a little like performing an exorcism.

Telling an LLM:

> "Make my software secure."

is a bit like an exorcist who has never read the Bible, studied theology, learned the ritual, or understood what they are dealing with walking up to a possessed person and saying:

> "Please stop being possessed."

The problem is not that the request is unclear. The problem is that the person giving the instruction has not supplied the knowledge, methods, constraints, tests, or standards required to determine what success actually means.

An AI model can generate code that *looks* secure. It can use reassuring words such as authentication, encryption, sanitization, validation, least privilege, and zero trust. That does not mean the resulting system is secure.

Secure software comes from a process: understanding threats, defining trust boundaries, identifying assets, selecting appropriate controls, following established standards, testing assumptions, verifying implementation, reviewing evidence, and continuously checking whether the system still satisfies its security requirements.

**AI can help enormously with that process. But it cannot replace the process.**

This starter kit exists to give both the human and the AI something better than "please make it secure": project knowledge, procedures, checklists, evidence requirements, security guidance, and explicit rules for deciding whether a result actually passed.

## What is in the kit?

- `00_QUICK_START` - one-page visual guide
- `01_BEGINNER_GUIDE` - plain-English onboarding
- `02_PROJECT_KNOWLEDGE_TEMPLATE` - a reusable RAG/project-knowledge structure
- `03_PROMPTS` - reusable AI prompts
- `04_SOFTWARE_WORKFLOW` - bounded software-development lifecycle
- `05_SECURITY` - secure baseline, assurance profiles, AI/RAG and supply-chain security
- `06_TEMPLATES` - requirements, threat models, decisions, tests, releases, and handoffs
- `07_CHECKLISTS` - operational checklists
- `08_EXAMPLES` - worked examples
- `09_REFERENCE` - glossary, RAG principles, and standards map
- `10_CHATGPT_SETUP` - ChatGPT-specific setup guidance
- `11_HANDBOOK` - printable handbook

## The core rule

> **AI output is a proposal until evidence proves the relevant result.**

The kit separates rules, requirements, architecture, security, decisions, mutable current state, and test/release evidence so that an AI-assisted project is less likely to silently lose constraints or rebaseline completed work.

## Assurance profiles

Use the lightest profile that is actually appropriate:

- **STARTER** - learning and local prototypes
- **PRODUCTION** - real users, internet exposure, or meaningful real data
- **HIGH ASSURANCE** - high-impact or regulated systems where failure can cause severe harm

See [`05_SECURITY/00_CHOOSE_YOUR_ASSURANCE_PROFILE.md`](05_SECURITY/00_CHOOSE_YOUR_ASSURANCE_PROFILE.md).

## Quick start

1. Read [`OPEN_THIS_FIRST.md`](OPEN_THIS_FIRST.md).
2. Open [`00_QUICK_START/QUICK_START_ONE_PAGE.pdf`](00_QUICK_START/QUICK_START_ONE_PAGE.pdf).
3. Read the beginner setup guide.
4. Copy `02_PROJECT_KNOWLEDGE_TEMPLATE` into your own project.
5. Choose an assurance profile.
6. Start with the supplied project prompt.
7. Build one small, bounded slice.
8. Verify it before continuing.

## What this project does not claim

This project does **not** guarantee that software produced with it is secure, safe, compliant, or production-ready. It is not a substitute for qualified security, legal, privacy, compliance, or safety expertise. Referenced standards remain authoritative over summaries in this repository.

## License and attribution

Except where otherwise noted, original content in this repository is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

You may copy, redistribute, adapt, and use the material commercially, provided you give appropriate credit, link to the license, and indicate if you made changes.

Preferred attribution:

> Secure Software Starter Kit by Kyle Gannon (GannoK), licensed under CC BY 4.0.

See [`LICENSE`](LICENSE) and [`ATTRIBUTION.md`](ATTRIBUTION.md).

## Contributing and security

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting changes. For security-related reports, see [`SECURITY.md`](SECURITY.md).

# Which standard do I need?

You usually do **not** need to read every standard.

## I am making a normal web application
Start with:
- this pack;
- OWASP Top 10;
- relevant OWASP ASVS requirements.

## I want a secure development process
Add:
- NIST SSDF;
- OWASP SAMM.

## I am publishing open-source software
Add:
- OpenSSF OSPS Baseline;
- OpenSSF Scorecard.

## I distribute build artifacts/packages
Add:
- SLSA;
- SPDX or CycloneDX SBOM;
- artifact signing/provenance appropriate to your ecosystem.

## My product includes LLMs, RAG, or AI agents
Add:
- OWASP GenAI LLM Top 10;
- explicit prompt-injection, retrieval-poisoning, data-boundary, tool-permission, and output-validation controls.

## My software handles money, health, identity, children, safety, critical infrastructure, regulated data, or other high-impact decisions
This starter pack is only a baseline.

Use qualified security, legal, privacy, safety, and compliance expertise appropriate to the domain and jurisdiction.

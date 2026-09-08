# Standards reference

Last reviewed: 2026-09-06

This starter pack uses established public standards as reference points. It does **not** claim that following this pack alone makes a project compliant.

## NIST Secure Software Development Framework (SSDF)

Stable final reference:
- NIST SP 800-218, SSDF Version 1.1
- https://csrc.nist.gov/pubs/sp/800/218/final

NIST also has an Initial Public Draft of SP 800-218 Rev. 1 / SSDF Version 1.2. Treat the draft as informative until finalized:
- https://csrc.nist.gov/pubs/sp/800/218/r1/ipd

Use SSDF as a high-level foundation for integrating secure practices through the software lifecycle.

## OWASP Application Security Verification Standard (ASVS)

Current stable release noted by OWASP at review time:
- ASVS 5.0.0
- https://owasp.org/www-project-application-security-verification-standard/

ASVS is useful when you need concrete application-security verification requirements.

## OWASP Top 10

Current web application awareness release:
- OWASP Top 10:2025
- https://owasp.org/Top10/

Use it as a risk-awareness baseline, not a complete security standard.

## OWASP SAMM

Software Assurance Maturity Model:
- https://owaspsamm.org/model/

SAMM organizes software security practices across Governance, Design, Implementation, Verification, and Operations.

## CISA Secure by Design

- https://www.cisa.gov/securebydesign

Core philosophy: manufacturers should take ownership of customer security outcomes, make products secure by default, and treat security as a product-quality responsibility.

## OpenSSF OSPS Baseline

Open Source Project Security Baseline:
- https://baseline.openssf.org/

Current version listed at review time:
- v2026.08.28

Useful for concrete open-source project security controls organized by maturity.

## OpenSSF Scorecard

- https://openssf.org/scorecard/

Useful for automated signals about open-source project security practices. A score is evidence, not a guarantee of safety.

## SLSA

Current approved specification at review time:
- SLSA v1.2
- https://slsa.dev/spec/v1.2/

SLSA provides incremental supply-chain security tracks and levels, including source and build provenance.

## SPDX

- https://spdx.dev/use/specifications/

Current version listed at review time:
- SPDX 3.0

SPDX is an ISO standard and can represent software supply-chain information including SBOM data.

## CycloneDX

- https://cyclonedx.org/specification/overview/

Current version listed at review time:
- CycloneDX 1.7

CycloneDX is a BOM standard designed for software/system supply-chain transparency.

## OWASP GenAI Security Project

Current LLM application guide at review time:
- OWASP GenAI LLM Top 10 2026
- https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

For RAG/AI systems, pay particular attention to:
- prompt injection;
- sensitive information disclosure;
- supply-chain risk;
- poisoning;
- improper output handling;
- excessive agency;
- retrieval/vector/embedding weaknesses.

## A practical way to use these

For a beginner project:
1. Use this starter pack as workflow scaffolding.
2. Use OWASP Top 10 for awareness.
3. Use ASVS requirements for concrete web-app verification.
4. Use NIST SSDF for development-process coverage.
5. Use OpenSSF/SLSA/SPDX/CycloneDX as the project and distribution maturity increases.
6. Use OWASP GenAI guidance whenever AI/RAG/agents are part of the system.

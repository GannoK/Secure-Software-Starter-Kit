# Dependencies, SBOMs, and software supply chain

Most modern software includes code you did not write.

That is normal, but it means your security depends partly on:
- package registries;
- maintainers;
- source repositories;
- CI/build systems;
- dependencies of dependencies;
- release artifacts.

## Before adding a dependency

Ask:
1. Do we really need it?
2. Is the package name correct?
3. Is the source/registry official?
4. Is it maintained?
5. Does it have known serious vulnerabilities?
6. What permissions/capabilities does it add?
7. Is there a simpler standard-library or existing-project option?

AI models can hallucinate package names. Verify unfamiliar packages independently.

## Locking and repeatability

Where supported:
- use lockfiles;
- pin release dependencies;
- keep runtime/build versions documented;
- avoid unexplained "latest" dependencies in production.

## SBOM

An SBOM is a Software Bill of Materials: a machine-readable inventory of components.

Common standards:
- SPDX
- CycloneDX

Generating an SBOM does not magically make software secure. It helps you know what is present so you can analyze and respond to vulnerabilities.

## Provenance

Build provenance records how an artifact was produced and from which inputs.

SLSA provides an incremental framework for strengthening source/build supply-chain assurance.

For a small project, simply recording exact source revision + repeatable build process is already useful. Increase assurance as the impact and distribution of the software grows.

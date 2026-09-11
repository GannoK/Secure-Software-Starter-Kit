# SLSA 1.2 Provenance Profile

SLSA is used here as a supply-chain assurance profile, not as a blanket claim that every project using this kit achieves a SLSA level.

## Starter

- Record the source repository and exact commit used for a release.
- Produce checksums for release artifacts.
- Preserve build/release instructions.
- Record the environment and dependency inputs that materially affect the artifact.

## Production

- Build release artifacts in CI rather than on an unrecorded developer workstation.
- Generate signed provenance/attestations for tagged releases.
- Keep workflow dependencies pinned to immutable commit SHAs.
- Restrict workflow token permissions to the minimum needed.
- Preserve provenance with the released artifact.

## High assurance

- Use isolated or ephemeral builders.
- Minimize mutable external build inputs.
- Verify provenance before downstream deployment or promotion.
- Record and review exceptions.
- Add reproducibility or independent rebuild evidence where practical.

## Verification

This repository's tagged-release workflow generates an archive, checksums, release evidence, and a GitHub/Sigstore-backed provenance attestation. Projects adopting the kit should adapt that workflow to their actual build artifacts rather than attesting an unrelated placeholder.

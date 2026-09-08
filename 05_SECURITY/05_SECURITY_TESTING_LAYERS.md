# Security testing layers

No single scanner proves software is secure.

Use layers.

## 1. Unit tests
Test individual functions.

## 2. Integration tests
Test components together.

## 3. End-to-end tests
Test the real user path.

## 4. Negative tests
Deliberately use bad/unauthorized/unexpected inputs.

Examples:
- invalid IDs;
- oversized inputs;
- missing authentication;
- wrong-user access;
- malformed files;
- expired tokens.

## 5. Static application security testing (SAST)
Analyzes source/code patterns.

## 6. Software composition analysis (SCA)
Looks for dependency vulnerabilities and related issues.

## 7. Secret scanning
Looks for accidentally committed credentials.

## 8. Dynamic testing (DAST)
Tests a running application from the outside.

## 9. Manual review
Humans or AI-assisted reviewers inspect design and code paths scanners may miss.

## 10. Threat-model verification
For each important threat, ask:
> What exact test proves the mitigation exists?

## Rule

A clean scanner result means:
> "This tool did not find a problem under this configuration."

It does not mean:
> "No vulnerability exists."

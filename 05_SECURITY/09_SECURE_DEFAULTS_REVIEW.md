# Secure Defaults Review

Use this review when introducing or materially changing a feature.

1. What is the safest reasonable default?
2. Does the user have to discover and enable a security feature that should be automatic?
3. Can a default expose data, credentials, network services, privileged operations, or destructive actions?
4. Does convenience weaken an authority or trust boundary?
5. Are insecure compatibility modes explicit and visibly risky?
6. Can the system fail closed where failure would otherwise create material risk?
7. Are secrets absent from logs, examples, defaults, and generated files?
8. Does the default minimize privileges and token permissions?
9. Are remote inputs, plugins, retrieved content, and AI/RAG context treated as untrusted where appropriate?
10. What regression test proves the secure default remains intact?

Record unresolved issues as `FAIL`, `MANUAL`, `UNKNOWN`, or a time-bounded `WAIVED` exception. Do not silently call them PASS.

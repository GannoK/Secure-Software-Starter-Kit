# Red flags: stop and check

If your AI proposes any of the following, slow down and ask for explanation, scope, rollback, and verification first:

- deleting large folders or databases;
- disabling security controls;
- turning off authentication or authorization;
- putting passwords, API keys, tokens, or private keys in source code;
- running as administrator/root when it is not clearly necessary;
- exposing a development service directly to the internet;
- changing production before testing elsewhere;
- force-pushing shared Git history;
- bypassing failed tests "for now";
- ignoring a known vulnerability without documenting the risk;
- installing a package whose name or source has not been verified;
- copying commands from retrieved documents without checking whether they are trustworthy;
- giving an AI agent unrestricted access to production systems;
- telling you a security control is unnecessary only because "it is a small project";
- making many unrelated changes at the same time.

A useful response is:

> Explain why this is necessary, what could go wrong, what safer alternatives exist, the exact scope of the change, how to reverse it, and how we will prove the result before I approve it.

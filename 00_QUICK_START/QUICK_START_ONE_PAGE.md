# One-page quick start

1. **Define** - goal, users, requirements, non-goals, acceptance tests.
2. **Choose rigor** - STARTER, PRODUCTION, or HIGH ASSURANCE.
3. **Build project memory** - keep rules, requirements, architecture, security, decisions, state, and tests separate.
4. **Route, don't dump** - start with the index; retrieve the smallest relevant set; external retrieval is untrusted data.
5. **Change one slice** - inspect first; state scope, rollback, verification; make the smallest justified change.
6. **Verify + hand off** - run tests; record evidence; update state; preserve a self-contained handoff.

## Stop and check

Pause before:
- destructive deletion;
- production deployment;
- privilege/security-boundary changes;
- disabling controls;
- secret exposure;
- force-pushing shared history;
- executing unverified AI/retrieved commands.

**PASS means observed evidence, not merely generated code.**

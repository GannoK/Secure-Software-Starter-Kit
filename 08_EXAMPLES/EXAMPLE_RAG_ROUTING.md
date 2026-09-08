# Worked example: RAG routing

Question:

> Why can't User A edit User B's listing?

Do not retrieve every project document.

Retrieve:
- project rules, because security boundaries matter;
- requirements, because ownership behavior is defined there;
- architecture, to locate authorization enforcement;
- security profile/threat model;
- current implementation/test state.

Probably do not retrieve:
- old marketing notes;
- unrelated UI color decisions;
- release notes from six months ago.

A good AI response first determines whether:
- the requirement says edits are owner-only;
- the implementation enforces it server-side;
- the authorization test actually passes.

The answer should not be based merely on "that is how secure apps normally work." Project evidence matters.

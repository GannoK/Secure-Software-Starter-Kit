# STARTER profile

Purpose: make beginner projects safer **without making learning impossible**.

## Required

### Project clarity
- [ ] Project goal and non-goals are written.
- [ ] Important requirements have acceptance tests.
- [ ] Sensitive data is identified.
- [ ] Unknowns are explicitly labeled.

### Source control
- [ ] Git or equivalent source control is used.
- [ ] Important working changes are committed in small checkpoints.
- [ ] Real secrets are never committed.

### Code and data
- [ ] Inputs are validated.
- [ ] Parameterized database APIs are used.
- [ ] Passwords/tokens/keys are outside source code.
- [ ] Dangerous file/path or command operations are narrowly scoped.
- [ ] Authentication/authorization uses maintained framework/library mechanisms when possible.

### Dependencies
- [ ] AI-suggested package names are independently verified.
- [ ] Official package sources are used.
- [ ] A lockfile or equivalent is committed where supported.

### Verification
- [ ] Important happy paths are tested.
- [ ] At least basic negative/error tests exist.
- [ ] The AI may not declare PASS without observed evidence.
- [ ] A backup exists for any irreplaceable project data.

### AI/RAG
- [ ] Retrieved text is treated as untrusted data.
- [ ] External documents cannot override project rules.
- [ ] Generated commands/code are reviewed before execution.

## Recommended

- secret scanning;
- dependency vulnerability scanning;
- static analysis;
- a simple threat model;
- a handoff after long sessions.

## Not sufficient for

Do not treat STARTER as sufficient for a public service with sensitive real-user data.

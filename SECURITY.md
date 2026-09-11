# Security Policy

## Supported versions

Security corrections are applied to the current maintained release and the default branch. Older snapshots may not receive backports unless explicitly stated.

## Scope

This repository is primarily guidance, templates, prompts, examples, and reference material. Security issues can still matter: unsafe command examples, insecure defaults, misleading security claims, dependency guidance that creates avoidable risk, prompt-injection weaknesses in recommended workflows, integrity-check bypasses, or instructions that could cause destructive behavior are all valid security concerns.

## Reporting a security issue

If a report contains sensitive exploit details, credentials, private data, or a technique that would be unsafe to publish immediately, **do not include those details in a public issue**.

Use GitHub's private vulnerability reporting or Security Advisory mechanism when it is available for this repository. If no private channel is available, open a minimal public issue stating that you have a security concern and need a private reporting channel, without including sensitive details.

For non-sensitive documentation or security-guidance defects, a normal GitHub issue is appropriate.

## What to include

Please provide enough information to reproduce or evaluate the concern:

- affected file and section;
- the unsafe or incorrect behavior;
- realistic impact;
- assumptions required for exploitation or harm;
- a safer alternative, if known;
- references or evidence supporting the report.

## Handling states

Reports may be tracked as `RECEIVED`, `TRIAGED`, `CONFIRMED`, `REMEDIATION_IN_PROGRESS`, `RESOLVED`, or `NOT_APPLICABLE`. These states are workflow labels, not a guaranteed response-time SLA.

## Response philosophy

Security claims should be evidence-based. A proposed fix is not considered complete merely because it sounds safer; the relevant behavior should be verified and regressions considered.

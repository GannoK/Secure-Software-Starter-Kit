# Architecture

## System overview

[Plain-English description.]

## Components

| Component | Purpose | Trust level | Data handled |
|---|---|---|---|
| [component] | [purpose] | [trusted/untrusted/mixed] | [data] |

## Data flow

1. [User or system sends...]
2. [Component processes...]
3. [Data is stored...]
4. [Result returns...]

## Trust boundaries

Document every place where data crosses between:
- browser and server;
- public internet and private network;
- application and database;
- application and third-party API;
- user and administrator;
- AI model and tool;
- AI system and retrieved knowledge;
- development and production.

## External dependencies

- [Service/library] — purpose — owner — version/pinning strategy

## Failure behavior

For each critical component:
- What happens if it is unavailable?
- Does the system fail safely?
- Is data corrupted or only delayed?
- Can the operator recover?

## Architecture decisions

Important accepted decisions belong in `60_DECISIONS.md`.

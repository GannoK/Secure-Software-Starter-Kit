# Threat modeling for normal people

Threat modeling means asking, **"How could this system fail or be abused before we build too much of it?"**

You do not need to be a security expert to start.

## Step 1 — What matters?

List assets:
- accounts;
- private messages;
- money;
- files;
- personal information;
- administrator privileges;
- API keys;
- source code;
- infrastructure.

## Step 2 — Who or what could cause harm?

Examples:
- anonymous attacker;
- malicious user;
- compromised user account;
- stolen administrator account;
- bad dependency;
- compromised third-party API;
- accidental developer mistake;
- malicious uploaded document;
- malicious retrieved AI/RAG document.

## Step 3 — Where are the boundaries?

Draw arrows between:
- user -> browser/app;
- app -> API/server;
- server -> database;
- server -> external service;
- AI -> retrieved knowledge;
- AI -> tools;
- developer -> production.

Every arrow is worth asking:
- Who is allowed?
- How do we authenticate them?
- What can they do?
- What input do we trust?
- What if the other side lies or is compromised?

## Step 4 — Abuse stories

Write simple stories:

> A user changes an ID in a URL and reads another user's private record.

> A malicious uploaded document contains instructions that manipulate an AI agent.

> A compromised dependency steals a build token.

## Step 5 — Turn threats into requirements

Threat:
> Users can read other users' data.

Requirement:
> Every private-record request must verify that the authenticated user is authorized for that exact record.

Test:
> Create two users. Confirm User A receives a denial when requesting User B's record.

That is threat modeling.

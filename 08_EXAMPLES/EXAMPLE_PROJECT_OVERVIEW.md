# Worked example: Neighborhood Tool Lending App

Imagine a beginner wants to build:

> A small web app where neighbors can list tools and request to borrow them.

## Project goal

Let registered neighbors list tools and request a loan from the tool owner.

## First-release non-goals

- no payments;
- no identity-document storage;
- no automatic door/lock integration;
- no public location sharing.

## Requirements

REQ-001:
A registered user can create a tool listing.

REQ-002:
Only the listing owner can edit or delete that listing.

REQ-003:
A user can request to borrow another user's tool.

REQ-004:
Exact home addresses are not publicly displayed.

## Security thinking

Asset:
private account and contact information.

Threat:
User A changes a listing ID and attempts to edit User B's listing.

Mitigation:
The server checks ownership for every edit/delete request.

Test:
Create User A and User B. Authenticate as A. Attempt to edit B's listing. Expect HTTP 403 or equivalent denial and no database change.

## First implementation slice

Not:
> Build the entire app.

Instead:
1. project skeleton;
2. local database;
3. user table;
4. one authenticated "create listing" API path;
5. authorization and validation tests;
6. simple UI form.

Then verify it before adding borrowing requests.

This is the mindset the starter pack is designed to teach.

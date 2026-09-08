# Requirements

## Users

Adults in one neighborhood who want to lend or borrow ordinary household tools.

## Must-have requirements

### REQ-001 - Registration and sign-in
A user can create an account and sign in.

Acceptance:
- valid credentials create an authenticated session;
- wrong credentials do not;
- private pages reject unauthenticated access.

### REQ-002 - Create listing
An authenticated user can create a tool listing with name, description, category, and availability flag.

Acceptance:
- valid listing is stored;
- missing required name is rejected;
- unauthenticated creation is rejected.

### REQ-003 - Owner-only modification
Only the listing owner can edit or delete a listing.

Acceptance:
- owner can edit;
- another authenticated user receives denial;
- denied request causes no database modification.

### REQ-004 - Borrow request
An authenticated user can request to borrow another user's available tool.

Acceptance:
- request is stored as pending;
- user cannot request their own listing;
- unavailable listing cannot receive a new request.

### REQ-005 - Owner approval
Listing owner can approve or reject pending requests for their listing.

### REQ-006 - Privacy
Exact home address is not part of the public listing.

## Nonfunctional requirements

- password storage uses framework-supported strong password hashing;
- networked production uses HTTPS;
- authorization tests are automated;
- local development uses fake data;
- production data is backed up.

## Non-goals

Payments, identity-document collection, public exact location, delivery logistics.

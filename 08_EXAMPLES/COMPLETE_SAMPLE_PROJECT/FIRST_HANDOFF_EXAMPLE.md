# Example handoff

Project: Neighborhood Tool Lending App

## Objective

Build the smallest secure first implementation slice for creating tool listings.

## Accepted constraints

- exact addresses are not public;
- server-side authorization is authoritative;
- no custom auth cryptography;
- no payments in v1;
- public release requires PRODUCTION assurance profile.

## Verified documentation state

The project knowledge set defines requirements, architecture, threats, decisions, and an explicit NOT READY release state.

## Exact next action

Create a local project skeleton and implement only REQ-002 create-listing behavior plus validation/tests.

## Verification

The slice passes only when:
- authenticated creation succeeds;
- missing required name fails safely;
- unauthenticated creation is denied;
- test results are observed;
- current-state/test documents are updated with evidence.

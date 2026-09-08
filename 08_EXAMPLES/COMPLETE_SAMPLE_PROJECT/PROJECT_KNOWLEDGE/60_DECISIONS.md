# Decision Log

## DEC-001 - No exact public addresses

Status: accepted

Decision:
v1 does not store or expose an exact home address as part of a public listing.

Rationale:
the core lending workflow does not require public exact location, and omitting it reduces privacy risk.

## DEC-002 - Server-side authorization is authoritative

Status: accepted

Decision:
UI visibility is convenience only. Every protected object operation is authorized by the API/server.

Rationale:
a user controls their browser and can manually call APIs.

## DEC-003 - No custom authentication cryptography

Status: accepted

Decision:
use maintained framework/library primitives and established password hashing.

## DEC-004 - No payments in v1

Status: accepted

Rationale:
payments introduce substantially more security, fraud, compliance, and operational scope than required for the first useful release.

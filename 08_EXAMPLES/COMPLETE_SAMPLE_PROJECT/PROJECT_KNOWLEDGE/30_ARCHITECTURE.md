# Architecture

## Overview

A conventional three-layer web application:

Browser -> Web/API application -> PostgreSQL database

## Components

| Component | Purpose | Trust |
|---|---|---|
| Browser UI | user interaction | untrusted client |
| Web/API | validation, authentication, authorization, business logic | trusted application boundary |
| PostgreSQL | durable application state | trusted data store |
| Email provider | account email/notification delivery | external service |

## Data flow

1. Browser sends input over HTTPS.
2. API authenticates the user when required.
3. API validates the request.
4. API performs server-side authorization.
5. API uses parameterized database access.
6. Response contains only data authorized for that user.

## Trust boundaries

- Browser -> API: all client input is untrusted.
- API -> database: use constrained DB credentials and parameterized access.
- API -> email provider: secrets stay server-side.
- Deployment/operator -> production: privileged boundary requiring separate controls.

## Failure behavior

- Database unavailable: return controlled service error; do not pretend mutation succeeded.
- Email unavailable: account workflow records delivery failure/retry state rather than corrupting core data.
- Authorization failure: deny without revealing protected object details.

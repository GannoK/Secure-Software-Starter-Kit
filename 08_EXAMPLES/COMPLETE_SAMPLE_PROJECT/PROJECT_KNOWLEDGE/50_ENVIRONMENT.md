# Environment

These are documented expectations, not live proof.

## Development

- OS: developer choice
- Language: Python 3.13
- Framework: FastAPI
- ORM: SQLAlchemy
- Database: PostgreSQL
- Tests: pytest
- Source control: Git

## Production candidate

- Linux container runtime
- managed PostgreSQL
- HTTPS reverse proxy/platform ingress
- protected environment secrets
- application process runs without root privileges

## Freshness rule

Exact package versions, branch, commit, deployment health, and running configuration must be checked live before consequential changes.

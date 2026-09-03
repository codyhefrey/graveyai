# Phase 11 — Database Persistence

## Implemented foundation

The memory subsystem now has a PostgreSQL adapter with:

- parameterized SQL;
- explicit ownership filtering and owner-safe updates;
- scope filtering;
- expiration filtering;
- deterministic ordering;
- metadata storage as JSONB;
- indexes for owner/scope and expiration;
- schema initialization support;
- versioned SQL migrations, including the pgvector foundation;
- PostgreSQL integration coverage in CI.

## Production hardening still required

This adapter is an implementation foundation, not a declaration of production readiness. Before stable deployment, GraveyAI must add:

- migration version tracking/runner and rollback policy;
- managed connection pooling;
- formal transaction/error handling policy;
- backup/restore verification;
- retention cleanup jobs;
- encryption and infrastructure controls;
- observability;
- load/performance testing;
- row-level security or an equivalent defense-in-depth authorization mechanism where appropriate;
- production embedding generation and vector retrieval lifecycle.

## Security boundary

Every read, delete, and update operation is scoped by `owner_id`. Application authentication/authorization remains responsible for establishing the caller identity; the repository is an additional data-layer boundary and must not be treated as the sole authorization mechanism.

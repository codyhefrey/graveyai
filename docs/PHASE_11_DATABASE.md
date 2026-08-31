# Phase 11 — Database Persistence

## Implemented foundation

The memory subsystem now has a PostgreSQL adapter with:

- parameterized SQL;
- explicit ownership filtering;
- scope filtering;
- expiration filtering;
- deterministic ordering;
- metadata storage as JSONB;
- indexes for owner/scope and expiration;
- schema initialization support;
- owner-scoped deletion.

## Production hardening still required

This adapter is an implementation foundation, not a declaration of production readiness. Before stable deployment, GraveyAI must add:

- formal versioned database migrations;
- managed connection pooling;
- transaction/error handling policy;
- PostgreSQL integration tests;
- backup/restore verification;
- retention cleanup jobs;
- encryption and infrastructure controls;
- observability;
- load/performance testing;
- row-level security or an equivalent defense-in-depth authorization mechanism where appropriate;
- pgvector schema and embedding lifecycle.

## Security boundary

Every read and delete operation is scoped by `owner_id`. Application authentication/authorization remains responsible for establishing the caller identity; the repository is an additional data-layer boundary and must not be treated as the sole authorization mechanism.

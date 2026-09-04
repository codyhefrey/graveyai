# Phase 11 Persistence Migration

The memory subsystem uses a provider-neutral persistence contract.

## Production target

```text
Memory Service
      ↓
PersistentMemoryRepository
      ↓
PostgreSQL Adapter
      ↓
PostgreSQL
      ├── memory_items
      ├── provenance
      ├── retention metadata
      └── authorization metadata

Future retrieval extension
      ↓
pgvector / hybrid retrieval
```

## Migration requirements

Before enabling persistent production memory:

1. Add database migrations.
2. Define indexes and authorization constraints.
3. Encrypt data in transit and protect storage credentials.
4. Implement parameterized queries/ORM access.
5. Add transaction and concurrency behavior.
6. Add deletion/retention jobs.
7. Add backup and restoration procedures.
8. Add integration tests against a disposable PostgreSQL instance.
9. Validate tenant isolation and deletion correctness.
10. Measure latency and storage growth.

The current `PostgresMemoryRepository` is deliberately an adapter boundary and does not claim to provide production persistence yet.

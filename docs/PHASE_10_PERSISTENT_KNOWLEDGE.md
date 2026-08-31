# Phase 10 — Persistent Knowledge & Distributed Vector Intelligence

## Status

Architecture and implementation specification.

## Objective

Establish a production-oriented knowledge subsystem in which GraveyAI can persist documents and metadata, create deterministic content identities, generate embeddings through replaceable providers, perform semantic retrieval, enforce access boundaries, and preserve provenance throughout the retrieval lifecycle.

Phase 10 converts the current dependency-light RAG foundation into a persistence-ready architecture without coupling the application to one vector database, embedding vendor, or deployment topology.

## Design principles

1. **Knowledge is data, not model memory.** Source material remains independently addressable and auditable.
2. **Embeddings are derived artifacts.** They can be regenerated when models change.
3. **Provenance survives transformation.** Chunking, embedding, indexing, and retrieval must preserve source identity.
4. **Tenant boundaries are explicit.** A user's private knowledge must not leak across authorization boundaries.
5. **Retrieval is replaceable.** In-memory development retrieval and production vector search implement the same logical contract.
6. **Distributed storage is eventual infrastructure.** The API must not require a particular database topology.
7. **Reproducibility matters.** Embedding model/version, chunking configuration, and ingestion metadata are recorded.

## Target architecture

```text
                         KNOWLEDGE API
                              │
                     Authentication/Policy
                              │
                              ▼
                       Ingestion Service
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
        Validation         Chunking       Metadata
             │                │                │
             └────────────────┼────────────────┘
                              ▼
                    Content Identity / Hash
                              │
                              ▼
                    Embedding Abstraction
                              │
               ┌──────────────┼──────────────┐
               ▼              ▼              ▼
          Local/Mock      Provider A      Provider B
               │              │              │
               └──────────────┼──────────────┘
                              ▼
                    Vector Storage Contract
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
            PostgreSQL +                Future
              pgvector                backends
                 │                         │
                 └────────────┬────────────┘
                              ▼
                       Retrieval Service
                              │
                       Authorization
                              │
                       Ranking / Filters
                              │
                              ▼
                   Evidence + Provenance
                              │
                              ▼
                           AI Core
```

## Logical data model

A production knowledge record should conceptually contain:

- `document_id`
- `owner_id` / tenant scope
- source URI or source descriptor
- title and metadata
- content hash
- chunk identifier
- chunk text or protected reference
- embedding vector reference
- embedding model and version
- chunking strategy/version
- creation and ingestion timestamps
- provenance metadata
- authorization metadata
- lifecycle status

Sensitive source content should not be logged by default.

## Retrieval contract

The retrieval interface should accept a query, optional filters, tenant/user scope, and result limits. Results should return ranked chunks together with source identity, relevance information, and provenance metadata required by the application.

The contract must remain independent of PostgreSQL, pgvector, OpenSearch, a hosted vector service, or any specific embedding provider.

## Retrieval lifecycle

```text
User Query
   ↓
Authenticate
   ↓
Authorize Knowledge Scope
   ↓
Normalize Query
   ↓
Generate Query Embedding
   ↓
Vector / Hybrid Retrieval
   ↓
Metadata + Permission Filtering
   ↓
Ranking
   ↓
Evidence Assembly
   ↓
Provenance Validation
   ↓
AI Reasoning Context
```

## Distributed intelligence direction

As GraveyAI becomes federated, knowledge services may be distributed across regions. The first implementation should keep storage and retrieval interfaces local and deterministic. Later federation can add:

- regional indexes;
- replicated metadata;
- signed knowledge advertisements;
- policy-aware remote retrieval;
- cache locality;
- replication health;
- conflict handling;
- encrypted transport;
- provenance synchronization.

Remote knowledge must never bypass local authorization policy merely because a remote node is trusted.

## Security requirements

- Enforce tenant/user authorization before retrieval.
- Prevent cross-tenant vector leakage.
- Protect embedding and metadata stores.
- Never commit provider credentials.
- Treat retrieved documents as untrusted input to prompt construction.
- Defend against prompt injection in retrieved content.
- Limit document size and ingestion resource consumption.
- Record security-relevant ingestion and retrieval events.
- Support deletion and retention policies.

## Evaluation requirements

Phase 10 should introduce measurable retrieval quality rather than relying only on subjective responses.

Track, where applicable:

- recall@k;
- precision@k;
- hit rate;
- ranking quality;
- latency;
- ingestion throughput;
- embedding cost;
- stale-index rate;
- authorization failure rate.

A retrieval benchmark corpus should be versioned separately from production user data.

## Migration path

```text
Current RAG foundation
        ↓
Stable storage/retrieval contracts
        ↓
Persistent document metadata
        ↓
Embedding abstraction
        ↓
PostgreSQL + pgvector adapter
        ↓
Hybrid retrieval + reranking
        ↓
Evaluation benchmark
        ↓
Regional replication
        ↓
Federated retrieval
```

## Definition of done

Phase 10 is complete when persistent ingestion, embedding, retrieval, authorization, provenance preservation, automated tests, evaluation metrics, failure behavior, configuration boundaries, and a documented production migration path are implemented and validated.

Phase 10 does **not** claim that distributed vector infrastructure is already production-ready until those gates are met.

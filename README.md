# GraveyAI

> **A provider-agnostic, provenance-aware AI system engineered from first principles for trustworthy intelligence, multilingual interaction, voice, knowledge retrieval, and future autonomous capabilities.**

## The engineering vision

GraveyAI is not a collection of disconnected features. It is one evolving system with explicit architectural boundaries: identity, security, intelligence, knowledge, multimodal interaction, provenance, infrastructure, and eventually autonomous agents.

The guiding principle is simple: **design the contracts first, isolate dependencies, make failure explicit, preserve provenance, and evolve infrastructure without rewriting the intelligence layer.**

Individual phases are milestones in one engineering journey—not separate products.

## Architecture at a glance

```text
                         ┌────────────────────────┐
                         │        CLIENTS         │
                         │ Web • Mobile • Voice   │
                         └────────────┬───────────┘
                                      │
                                      ▼
                         ┌────────────────────────┐
                         │   SECURITY BOUNDARY    │
                         │ Identity • Auth • API  │
                         └────────────┬───────────┘
                                      │
                   ┌──────────────────┼──────────────────┐
                   ▼                  ▼                  ▼
              ┌─────────┐        ┌─────────┐        ┌──────────┐
              │  CHAT   │        │  VOICE  │        │DOCUMENTS │
              └────┬────┘        └────┬────┘        └────┬─────┘
                   └──────────────────┼──────────────────┘
                                      ▼
                         ┌────────────────────────┐
                         │    INTELLIGENCE CORE   │
                         │ AI • Orchestration     │
                         │ Tools • Memory         │
                         └────────────┬───────────┘
                                      │
                           ┌──────────┴──────────┐
                           ▼                     ▼
                    ┌────────────┐       ┌────────────┐
                    │    RAG     │       │ AI MODELS  │
                    │ Knowledge  │       │ Providers  │
                    └─────┬──────┘       └────────────┘
                          │
                          ▼
                    ┌────────────┐
                    │ PROVENANCE │
                    │   + TRUST  │
                    └─────┬──────┘
                          ▼
                    ┌────────────┐
                    │GraveyChain │
                    └────────────┘
```

## Architectural laws

### 1. Contracts before vendors
Core interfaces define capabilities. Vendor SDKs live behind adapters. Changing an AI, STT, TTS, database, or retrieval provider should not require rewriting the application.

### 2. Security at the boundary
Identity is established before protected application operations. Application logic consumes authenticated identity rather than owning credential storage.

### 3. Deterministic development
Mock providers remain first-class development dependencies so tests remain reproducible and do not require external services.

### 4. Knowledge must be traceable
Retrieved knowledge carries content identity and provenance metadata. Trust is designed into the data path rather than added after the fact.

### 5. Infrastructure must remain replaceable
Development services can evolve into PostgreSQL, pgvector, object storage, distributed queues, and production infrastructure while preserving stable application contracts.

### 6. Secrets never belong in source control
Credentials are configuration concerns. The repository contains interfaces and configuration rules—not production secrets.

### 7. Failure is part of the architecture
External services can fail, time out, reject requests, or become unavailable. Each boundary should have explicit validation, bounded failures, and useful diagnostics.

### 8. Observability is engineering, not decoration
Production evolution requires structured logs, metrics, traces, health checks, audit events, and evaluation signals.

### 9. Least privilege everywhere
Identity, documents, tools, memory, and future agent actions must have explicit authorization boundaries.

### 10. Evolution without rewrites
New capabilities should compose with the existing system. The goal is controlled architectural growth—not accumulating technical debt until the platform must be rebuilt.

## Engineering journey

```text
FOUNDATION
Architecture → Configuration → APIs → Testing
        ↓
SECURITY
Authentication → Identity → Authorization
        ↓
INTELLIGENCE
AI Provider → Reasoning → Orchestration
        ↓
KNOWLEDGE
RAG → Ingestion → Retrieval → Provenance
        ↓
MULTIMODAL
Text → Speech → Voice → Documents → Vision
        ↓
PERSISTENCE
PostgreSQL → Vector Search → Memory → User Data
        ↓
AGENCY
Tools → Workflows → Planning → Controlled Agents
        ↓
TRUST
Evaluation → Safety → Auditing → GraveyChain
        ↓
SCALE
Docker → CI/CD → Observability → Distributed Infrastructure
        ↓
ADVANCED SYSTEMS
Multilingual Intelligence → Quantum-ready Security → Global Platform
```

## Current milestone

**Phase 8 — Provenance-aware RAG foundation.** GraveyAI can ingest documents through the RAG pipeline, preserve SHA3-256 provenance metadata associated with GraveyChain, and expose authenticated retrieval endpoints. The current retriever is intentionally dependency-light so production semantic retrieval can be introduced without changing the public API contract.

### Phase 8 endpoints

- `POST /api/v1/rag/documents` — authenticated document ingestion.
- `POST /api/v1/rag/search` — authenticated knowledge retrieval.

## Technology direction

- **Frontend:** Next.js + TypeScript
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **Vector search:** pgvector
- **AI:** provider-agnostic interface + model adapters
- **Voice:** provider-agnostic STT/TTS interfaces
- **Infrastructure:** Docker
- **Testing:** Pytest + API tests
- **CI:** GitHub Actions

## Repository structure

```text
graveyai/
├── .github/workflows/       # CI/CD automation
├── backend/
│   ├── app/
│   │   ├── api/v1/          # Stable API boundary
│   │   ├── ai/              # AI provider abstraction/adapters
│   │   ├── auth/            # Identity/authentication boundary
│   │   ├── core/            # Configuration and application primitives
│   │   ├── rag/             # Knowledge ingestion/retrieval/provenance
│   │   └── voice/           # STT/TTS abstraction and orchestration
│   └── tests/               # Automated verification
├── docs/                    # Architecture and engineering decisions
├── frontend/                # Client applications
└── docker-compose.yml       # Local infrastructure
```

## Definition of done

A GraveyAI capability is not considered complete merely because its happy path works. A mature capability should have a clear contract, validation, authentication/authorization where required, deterministic tests, failure handling, configuration boundaries, observability hooks, and a migration path from development to production infrastructure.

**GraveyAI is being built as a system first and a feature set second.**

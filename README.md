# GraveyAI

> **A provider-agnostic, provenance-aware AI platform engineered for research, analysis, decision support, learning, knowledge discovery, and multimodal human interaction.**

**From Africa. By Africa. For the World. For Everyone.**

## Project position

GraveyAI is not a collection of disconnected features and not merely an LLM wrapper. It is an evolving AI platform designed around explicit architectural boundaries for identity, security, intelligence, knowledge, multimodal interaction, provenance, resilience, and future controlled autonomy.

The engineering objective is to build a system that researchers, professionals, organizations, students, and everyday users can use to understand information, analyze evidence, conduct research, explore ideas, and make better-informed decisions.

## Engineering principles

- **Contracts before vendors** — core interfaces isolate external providers.
- **Security at the boundary** — authenticated identity precedes protected operations.
- **Evidence before assertion** — research-oriented outputs should distinguish evidence, inference, assumptions, and uncertainty.
- **Provenance by design** — important knowledge objects retain source and integrity metadata.
- **Decentralized by design; resilient by architecture** — avoid unnecessary single points of failure without forcing every subsystem onto a blockchain.
- **Least privilege** — users, services, documents, tools, memory, and agents receive only required authority.
- **Failure is part of the architecture** — outages, timeouts, partitions, provider failures, and compromised nodes are design cases.
- **Deterministic development** — mocks and local implementations keep tests reproducible.
- **Infrastructure remains replaceable** — model, voice, retrieval, storage, and cloud providers remain adapter boundaries.
- **Measured claims only** — implemented, tested, validated, production-ready, planned, and research capabilities are explicitly distinguished.

## Architecture at a glance

```text
                         ┌────────────────────────┐
                         │        CLIENTS         │
                         │ Web • Mobile • Voice   │
                         │ Research • Data • API  │
                         └────────────┬───────────┘
                                      │
                                      ▼
                         ┌────────────────────────┐
                         │   SECURITY BOUNDARY    │
                         │ Identity • Auth • API  │
                         └────────────┬───────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
                 Research          Voice             Documents
                    │                 │                 │
                    └─────────────────┼─────────────────┘
                                      ▼
                         ┌────────────────────────┐
                         │    INTELLIGENCE CORE   │
                         │ Models • Reasoning     │
                         │ Orchestration • Tools  │
                         └────────────┬───────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
                  RAG              Memory            Analysis
                    │                 │                 │
                    └─────────────────┼─────────────────┘
                                      ▼
                         ┌────────────────────────┐
                         │   TRUST + PROVENANCE   │
                         │ Evidence • Integrity   │
                         │ Audit • GraveyChain    │
                         └────────────┬───────────┘
                                      │
                                      ▼
                         ┌────────────────────────┐
                         │ DISTRIBUTED FOUNDATION │
                         │ Nodes • Discovery      │
                         │ Replication • Recovery │
                         └────────────────────────┘
```

## Research and decision-support model

GraveyAI is intended to support serious analytical workflows rather than simply generate fluent answers.

```text
Question / Problem
       ↓
Acquire Evidence
       ↓
Validate Inputs
       ↓
Retrieve Relevant Knowledge
       ↓
Analyze / Reason
       ↓
Identify Assumptions
       ↓
Quantify or Explain Uncertainty
       ↓
Produce Findings
       ↓
Expose Sources / Provenance
       ↓
Human Review and Decision
```

The system should help users make better decisions without presenting itself as an unquestionable authority.

## Release strategy

Development phases are engineering milestones. **Releases are validated, versioned product states.** A phase may span multiple releases, and a release may consolidate work from multiple phases.

### Release families

| Release | Working designation | Primary objective |
|---|---|---|
| **v0.1.x** | Genesis | Initial architecture and foundational services |
| **v0.2.x** | Foundation | APIs, configuration, security and testing foundations |
| **v0.3.x** | Intelligence | Model/provider abstraction and reasoning infrastructure |
| **v0.4.x** | Knowledge | RAG, ingestion, retrieval and provenance |
| **v0.5.x** | Voice | Multimodal speech interfaces and provider abstraction |
| **v0.6.x** | Federation | Distributed identity, trust and service discovery |
| **v0.7.x** | Memory | Persistent knowledge, vector search and contextual memory |
| **v0.8.x** | Agents | Tools, workflows and controlled agent orchestration |
| **v0.9.x** | Research | Research workflows, evaluation and reproducibility |
| **v1.0.x** | Initial Stable | Production-grade initial platform |
| **v2.x+** | Evolution | Distributed intelligence and advanced capabilities |

These designations are roadmap targets unless a corresponding release is published and documented.

### Release channels

- **Experimental** — research and architectural experiments.
- **Alpha** — incomplete capabilities suitable for controlled development use.
- **Beta** — integrated capabilities undergoing broader validation.
- **Stable** — documented, tested, supported capability set.

### Semantic versioning

GraveyAI follows the intent of semantic versioning:

```text
MAJOR.MINOR.PATCH
  │     │     └── Compatible fixes
  │     └──────── Backward-compatible capabilities
  └────────────── Breaking API or architectural changes
```

### Release gates

A release should not be declared mature merely because the happy path works. Release readiness should consider:

- automated tests;
- API compatibility;
- security checks;
- dependency review;
- configuration and secret hygiene;
- failure-path testing;
- documentation;
- observability;
- reproducibility;
- performance characteristics where applicable;
- known limitations and rollback/recovery procedures.

## Engineering lifecycle

```text
IDEA
 ↓
ARCHITECTURE
 ↓
INTERFACE / CONTRACT
 ↓
IMPLEMENTATION
 ↓
UNIT + INTEGRATION TESTS
 ↓
SECURITY / FAILURE REVIEW
 ↓
VALIDATION
 ↓
RELEASE CANDIDATE
 ↓
VERSIONED RELEASE
 ↓
OBSERVATION
 ↓
ITERATION
```

## Engineering journey

```text
FOUNDATION
Architecture → Configuration → APIs → Testing
        ↓
SECURITY
Authentication → Identity → Authorization
        ↓
INTELLIGENCE
AI Providers → Reasoning → Orchestration
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
RESILIENCE
Federation → Discovery → Replication → Recovery
        ↓
SCALE
Containers → CI/CD → Observability → Distributed Infrastructure
        ↓
ADVANCED SYSTEMS
Multilingual Intelligence → Post-quantum Readiness → Global Platform
```

## Current implementation status

**Phase 11 is an active development branch.** The repository contains foundational authentication, provider abstraction, voice, provenance-aware RAG, and controlled memory work. Phase 11 now includes explicit memory models and retention policy, a development store, a PostgreSQL persistence adapter boundary, versioned PostgreSQL/pgvector schema migrations, and provider-neutral embedding contracts.

The current RAG and embedding implementations remain dependency-light development implementations. Production semantic retrieval, production identity verification, persistent-memory operations, and distributed deployment require their respective release gates before being declared stable.

## Technology direction

- **Frontend:** Next.js + TypeScript
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **Vector search:** pgvector
- **AI:** provider-agnostic interfaces + model adapters
- **Voice:** provider-agnostic STT/TTS interfaces
- **Infrastructure:** Docker
- **Testing:** Pytest + API tests
- **CI:** GitHub Actions
- **Distributed systems:** federation, service discovery, replication and resilient routing

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
│   │   ├── memory/          # Controlled persistent/contextual memory
│   │   ├── rag/             # Knowledge ingestion/retrieval/provenance
│   │   └── voice/           # STT/TTS abstraction and orchestration
│   ├── migrations/          # Versioned database migrations
│   └── tests/               # Automated verification
├── docs/                    # Architecture, resilience and engineering decisions
├── frontend/                # Client applications
└── docker-compose.yml       # Local infrastructure
```

## Definition of done

A GraveyAI capability is complete only when its contract, implementation, validation, security boundary, failure behavior, configuration boundary, tests, documentation, and production migration path are understood and appropriately verified.

**GraveyAI is being built as a system first and a feature set second.**

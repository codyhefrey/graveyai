# GraveyAI

> An AI-powered knowledge and assistance platform built for trustworthy retrieval, multilingual interaction, voice capabilities, and practical everyday assistance.

## Vision

GraveyAI aims to make useful AI accessible through a single platform that can understand questions, retrieve trusted knowledge, work with documents, and eventually communicate through text and voice.

## Phase 1 — Foundation

This repository establishes the initial architecture for a production-oriented GraveyAI system.

### Planned capabilities

- AI conversational assistant
- Retrieval-Augmented Generation (RAG)
- Document ingestion and knowledge retrieval
- Multilingual interaction
- Voice input and output
- Authentication and user accounts
- Conversation history and memory
- AI safety and evaluation tooling
- Docker-based local development
- Automated testing and CI/CD

## Architecture

```text
                         ┌──────────────────┐
                         │     GraveyAI     │
                         │   AI Assistant   │
                         └────────┬─────────┘
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              ┌──────────┐  ┌──────────┐  ┌───────────┐
              │   Chat   │  │   Voice  │  │ Documents │
              └────┬─────┘  └────┬─────┘  └─────┬─────┘
                   └─────────────┼───────────────┘
                                 ▼
                         ┌───────────────┐
                         │   AI Engine   │
                         │    LLM + RAG  │
                         └───────┬───────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
              ┌──────────┐ ┌──────────┐ ┌────────────┐
              │PostgreSQL│ │ pgvector │ │ Knowledge  │
              │ Database │ │ Embeddings│ │    Base    │
              └──────────┘ └──────────┘ └────────────┘
```

## Technology direction

- **Frontend:** Next.js + TypeScript
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **Vector search:** pgvector
- **AI orchestration:** modular AI/RAG services
- **Infrastructure:** Docker
- **Testing:** Pytest + API tests
- **CI:** GitHub Actions

## Repository structure

```text
graveyai/
├── .github/workflows/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── ai/
│   │   ├── rag/
│   │   ├── models/
│   │   └── services/
│   └── tests/
├── frontend/
├── docs/
├── infrastructure/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Roadmap

- [x] Phase 1: Project foundation
- [ ] Phase 2: FastAPI backend and health API
- [ ] Phase 3: AI chat service
- [ ] Phase 4: RAG and document intelligence
- [ ] Phase 5: Web interface
- [ ] Phase 6: Authentication and user management
- [ ] Phase 7: Voice interface
- [ ] Phase 8: Evaluation, testing, and security hardening
- [ ] Phase 9: Cloud deployment
- [ ] Phase 10: Production readiness

## Development principles

1. Privacy and security by design.
2. Clear separation between application logic and AI providers.
3. Ground answers in retrieved evidence whenever possible.
4. Test critical behavior before adding complexity.
5. Keep the project modular so components can evolve independently.

## Status

**Early development — Phase 1.**

GraveyAI is an evolving open-source project. APIs, architecture, and implementation details may change as the system matures.

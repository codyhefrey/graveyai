# Phase 11 — Memory, Context & Personal Knowledge

## Objective

Define a controlled memory subsystem that enables GraveyAI to maintain useful continuity without treating all conversation data as permanent memory.

## Design principle

**Memory must be explicit, scoped, auditable, revocable, and policy-controlled.**

Memory is not equivalent to model weights and should remain outside the model unless explicitly supplied as context during an authorized operation.

## Memory classes

- **Session context** — temporary state for an active interaction.
- **User memory** — information explicitly retained for an individual account.
- **Research memory** — project-specific notes, findings, hypotheses, and references.
- **Organizational memory** — authorized institutional knowledge with explicit tenancy boundaries.
- **System knowledge** — curated platform knowledge managed independently from personal memory.

## Target architecture

```text
                    USER / APPLICATION
                            │
                            ▼
                     Memory Gateway
                            │
                   Authentication + Policy
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
           Session        User         Research
           Context       Memory         Memory
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                    Memory Policy Engine
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
              RETAIN              FORGET
                  │                   │
                  ▼                   ▼
             Authorized          Deletion /
              Retrieval          Expiration
                  │
                  ▼
              AI Context
```

## Memory lifecycle

```text
Candidate Information
        ↓
Classify
        ↓
Policy Check
        ↓
Explicit / Authorized Retention
        ↓
Store Metadata + Provenance
        ↓
Retrieve Only Within Scope
        ↓
Use as Context
        ↓
Audit
        ↓
Expire / Delete / Correct
```

## Required controls

- Explicit scope for every memory item.
- User/tenant authorization before retrieval.
- Retention and expiration policy.
- User-visible memory management.
- Deletion and correction mechanisms.
- Provenance and creation metadata.
- Protection against cross-user or cross-tenant retrieval.
- No silent elevation of ordinary conversation into permanent memory.
- Sensitive information should receive stricter policy treatment.
- Memory content is untrusted input and must be protected against prompt injection.

## Research mode

Research memory should support structured project continuity:

```text
Project
 ├── Questions
 ├── Sources
 ├── Hypotheses
 ├── Notes
 ├── Evidence
 ├── Findings
 ├── Contradictions
 ├── Decisions
 └── Open Problems
```

This enables GraveyAI to function as a persistent research assistant while preserving separation between source evidence, user interpretation, model-generated suggestions, and verified findings.

## Memory versus knowledge

Persistent knowledge and memory are related but distinct:

- **Knowledge** answers: "What information exists and where did it come from?"
- **Memory** answers: "What authorized context should GraveyAI retain for continuity?"

The system should be able to link them without conflating them.

## Evaluation

Memory quality should be measured by retrieval relevance, unwanted recall rate, stale-memory rate, deletion correctness, authorization correctness, latency, and user control—not merely by whether the model appears more conversational.

## Definition of done

Phase 11 is complete when memory classes, authorization boundaries, retention/deletion behavior, storage contracts, retrieval policy, tests, auditability, and user controls are implemented and validated.

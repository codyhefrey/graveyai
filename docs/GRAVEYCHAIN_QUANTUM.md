# GraveyChain + Quantum-Ready Architecture

## Purpose

GraveyAI will use **GraveyChain** as a trust and provenance layer. The chain is not used to store private document contents. Instead, it can anchor cryptographic fingerprints and metadata that allow a knowledge record to be independently verified.

## Knowledge integrity flow

```text
Document
  ↓
Normalize + chunk
  ↓
SHA3-256 fingerprint
  ↓
Embedding + vector index
  ↓
Retrieval
  ↓
AI answer
  ↓
Provenance metadata
  ↓
GraveyChain anchor
```

## Quantum-ready design

The project uses the term **quantum-ready** to mean cryptographic agility and a planned migration path toward post-quantum cryptography. It does not claim that the application performs quantum computation.

Design requirements:

- Keep hashing and signature algorithms replaceable.
- Use SHA3-256 for current content fingerprints.
- Keep a versioned provenance record.
- Design chain identity and signing interfaces so post-quantum algorithms can be introduced without redesigning the RAG layer.
- Never store API keys or private document contents on-chain.
- Evaluate standardized post-quantum algorithms such as ML-KEM and ML-DSA during the security phase.

## RAG implementation status

Phase 4 currently provides:

- deterministic document chunking
- SHA3-256 content fingerprints
- GraveyChain provenance records
- embedding-provider interface
- retrieval-provider interface
- an ingestion pipeline
- unit tests

Next iterations will connect embeddings to pgvector, persist documents/chunks, implement similarity retrieval, and anchor finalized provenance records through a real GraveyChain node or service.

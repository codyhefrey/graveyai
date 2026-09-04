-- GraveyAI Phase 11: semantic memory foundation
-- PostgreSQL migration 002
-- Requires the pgvector extension in environments where vector search is enabled.

CREATE EXTENSION IF NOT EXISTS vector;

ALTER TABLE memory_items
    ADD COLUMN IF NOT EXISTS embedding_model TEXT,
    ADD COLUMN IF NOT EXISTS embedding_model_version TEXT,
    ADD COLUMN IF NOT EXISTS embedding VECTOR(1536);

CREATE INDEX IF NOT EXISTS idx_memory_items_embedding_hnsw
    ON memory_items USING hnsw (embedding vector_cosine_ops)
    WHERE embedding IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_memory_items_embedding_model
    ON memory_items (embedding_model, embedding_model_version);

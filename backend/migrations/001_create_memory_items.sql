-- GraveyAI Phase 11: persistent memory foundation
-- PostgreSQL migration 001

CREATE TABLE IF NOT EXISTS memory_items (
    memory_id UUID PRIMARY KEY,
    owner_id TEXT NOT NULL,
    content TEXT NOT NULL,
    scope TEXT NOT NULL CHECK (scope IN ('session', 'user', 'research', 'organization')),
    source TEXT,
    created_at TIMESTAMPTZ NOT NULL,
    expires_at TIMESTAMPTZ,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE INDEX IF NOT EXISTS idx_memory_items_owner_scope
    ON memory_items (owner_id, scope);

CREATE INDEX IF NOT EXISTS idx_memory_items_expires_at
    ON memory_items (expires_at);

from app.rag.chunker import chunk_document
from app.rag.pipeline import RAGPipeline
from app.rag.provenance import fingerprint


def test_fingerprint_is_deterministic():
    assert fingerprint("hello") == fingerprint("hello")
    assert len(fingerprint("hello")) == 64


def test_chunk_document_creates_chunks():
    chunks = chunk_document("doc-1", "hello world " * 200, chunk_size=100, overlap=10)
    assert len(chunks) > 1
    assert chunks[0].document_id == "doc-1"
    assert chunks[0].content_hash


def test_pipeline_returns_provenance():
    chunks, provenance = RAGPipeline().ingest("doc-1", "GraveyAI knowledge")
    assert chunks
    assert provenance.chain == "GraveyChain"
    assert provenance.hash_algorithm == "SHA3-256"
    assert provenance.quantum_ready is True

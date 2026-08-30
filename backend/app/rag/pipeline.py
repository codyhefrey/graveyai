from app.rag.chunker import chunk_document
from app.rag.models import DocumentChunk, ProvenanceRecord
from app.rag.provenance import create_provenance


class RAGPipeline:
    """Coordinates ingestion now; embedding and persistence are injected later."""

    def ingest(self, document_id: str, text: str) -> tuple[list[DocumentChunk], ProvenanceRecord]:
        provenance = create_provenance(document_id, text)
        chunks = chunk_document(document_id, text)
        return chunks, provenance

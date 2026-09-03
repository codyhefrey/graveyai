import re

from app.rag.models import DocumentChunk, RetrievalResult
from app.rag.pipeline import RAGPipeline


class RAGService:
    """Development retrieval service with tenant-scoped in-memory state."""

    def __init__(self) -> None:
        self.pipeline = RAGPipeline()
        self._chunks_by_owner: dict[str, list[DocumentChunk]] = {}

    def ingest(
        self, owner_id: str, document_id: str, text: str
    ) -> tuple[list[DocumentChunk], object]:
        if not owner_id.strip():
            raise ValueError("owner_id is required")
        chunks, provenance = self.pipeline.ingest(document_id, text)
        self._chunks_by_owner.setdefault(owner_id, []).extend(chunks)
        return chunks, provenance

    def search(self, owner_id: str, query: str, top_k: int = 5) -> list[RetrievalResult]:
        if not owner_id.strip():
            raise ValueError("owner_id is required")
        terms = _terms(query)
        if not terms:
            return []
        results: list[RetrievalResult] = []
        for chunk in self._chunks_by_owner.get(owner_id, []):
            chunk_terms = _terms(chunk.text)
            overlap = len(terms & chunk_terms)
            if overlap:
                results.append(RetrievalResult(chunk, overlap / len(terms)))
        return sorted(results, key=lambda item: item.score, reverse=True)[:top_k]


def _terms(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9_]{2,}", text.lower()))

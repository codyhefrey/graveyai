import re

from app.rag.models import DocumentChunk, RetrievalResult
from app.rag.pipeline import RAGPipeline


class RAGService:
    """Development retrieval service built on the existing provenance-aware pipeline."""

    def __init__(self) -> None:
        self.pipeline = RAGPipeline()
        self._chunks: list[DocumentChunk] = []

    def ingest(self, document_id: str, text: str) -> tuple[list[DocumentChunk], object]:
        chunks, provenance = self.pipeline.ingest(document_id, text)
        self._chunks.extend(chunks)
        return chunks, provenance

    def search(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        terms = _terms(query)
        if not terms:
            return []
        results: list[RetrievalResult] = []
        for chunk in self._chunks:
            chunk_terms = _terms(chunk.text)
            overlap = len(terms & chunk_terms)
            if overlap:
                results.append(RetrievalResult(chunk, overlap / len(terms)))
        return sorted(results, key=lambda item: item.score, reverse=True)[:top_k]


def _terms(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9_]{2,}", text.lower()))

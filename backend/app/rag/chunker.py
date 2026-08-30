from app.rag.models import DocumentChunk
from app.rag.provenance import fingerprint


def chunk_document(document_id: str, text: str, chunk_size: int = 1200, overlap: int = 150) -> list[DocumentChunk]:
    """Split text into overlapping chunks suitable for embedding/retrieval."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and smaller than chunk_size")

    cleaned = " ".join(text.split())
    if not cleaned:
        return []

    chunks: list[DocumentChunk] = []
    start = 0
    index = 0
    step = chunk_size - overlap
    while start < len(cleaned):
        piece = cleaned[start : start + chunk_size]
        chunks.append(
            DocumentChunk(
                document_id=document_id,
                chunk_id=f"{document_id}:{index}",
                text=piece,
                content_hash=fingerprint(piece),
                metadata={"chunk_index": str(index)},
            )
        )
        index += 1
        start += step
    return chunks

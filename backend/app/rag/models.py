from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentChunk:
    document_id: str
    chunk_id: str
    text: str
    content_hash: str
    metadata: dict[str, str]


@dataclass(frozen=True)
class RetrievalResult:
    chunk: DocumentChunk
    score: float


@dataclass(frozen=True)
class ProvenanceRecord:
    document_id: str
    content_hash: str
    hash_algorithm: str = "SHA3-256"
    chain: str = "GraveyChain"
    quantum_ready: bool = True

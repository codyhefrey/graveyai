import hashlib

from app.rag.models import ProvenanceRecord


def fingerprint(content: str) -> str:
    """Create a deterministic SHA3-256 fingerprint for knowledge provenance."""
    return hashlib.sha3_256(content.encode("utf-8")).hexdigest()


def create_provenance(document_id: str, content: str) -> ProvenanceRecord:
    return ProvenanceRecord(
        document_id=document_id,
        content_hash=fingerprint(content),
    )

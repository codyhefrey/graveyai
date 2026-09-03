from app.rag.service import RAGService


def test_rag_service_isolates_documents_by_owner() -> None:
    service = RAGService()
    service.ingest("user-1", "private-doc", "private research material")

    assert service.search("user-1", "private research")
    assert service.search("user-2", "private research") == []


def test_rag_service_requires_owner() -> None:
    service = RAGService()

    try:
        service.search(" ", "query")
    except ValueError as exc:
        assert str(exc) == "owner_id is required"
    else:
        raise AssertionError("missing owner_id must be rejected")

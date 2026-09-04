from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
AUTH = {"Authorization": "Bearer development-token"}


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_requires_authentication() -> None:
    response = client.post("/api/v1/chat", json={"message": "Hello GraveyAI"})
    assert response.status_code == 401


def test_chat_with_development_identity() -> None:
    response = client.post(
        "/api/v1/chat",
        headers=AUTH,
        json={"message": "Hello GraveyAI"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["provider"] == "mock"
    assert "Hello GraveyAI" in body["response"]


def test_memory_lifecycle_is_authenticated_and_scoped() -> None:
    create = client.post(
        "/api/v1/memory",
        headers=AUTH,
        json={
            "content": "remember this research note",
            "scope": "research",
            "source": "api-test",
            "metadata": {"kind": "note"},
        },
    )
    assert create.status_code == 201
    memory = create.json()
    memory_id = memory["memory_id"]
    assert memory["scope"] == "research"
    assert memory["expires_at"] is not None

    fetched = client.get(f"/api/v1/memory/{memory_id}", headers=AUTH)
    assert fetched.status_code == 200
    assert fetched.json()["content"] == "remember this research note"

    listed = client.get("/api/v1/memory?scope=research", headers=AUTH)
    assert listed.status_code == 200
    assert any(item["memory_id"] == memory_id for item in listed.json()["items"])

    deleted = client.delete(f"/api/v1/memory/{memory_id}", headers=AUTH)
    assert deleted.status_code == 204

    missing = client.get(f"/api/v1/memory/{memory_id}", headers=AUTH)
    assert missing.status_code == 404


def test_memory_rejects_unsupported_scope() -> None:
    response = client.post(
        "/api/v1/memory",
        headers=AUTH,
        json={"content": "test", "scope": "unknown"},
    )
    assert response.status_code == 422

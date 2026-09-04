from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.api.v1.router import get_ai_provider, get_stt_provider, get_tts_provider
from app.core.config import Settings
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


def test_mock_providers_fail_closed_outside_development() -> None:
    settings = Settings(environment="production", ai_provider="mock")
    try:
        get_ai_provider(settings)
    except HTTPException as exc:
        assert exc.status_code == 503
    else:
        raise AssertionError("mock AI provider must be rejected outside development")

    voice_settings = Settings(environment="production", voice_stt_provider="mock")
    try:
        get_stt_provider(voice_settings)
    except HTTPException as exc:
        assert exc.status_code == 503
    else:
        raise AssertionError("mock STT provider must be rejected outside development")

    tts_settings = Settings(environment="production", voice_tts_provider="mock")
    try:
        get_tts_provider(tts_settings)
    except HTTPException as exc:
        assert exc.status_code == 503
    else:
        raise AssertionError("mock TTS provider must be rejected outside development")

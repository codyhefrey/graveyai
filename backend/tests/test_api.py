from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat() -> None:
    response = client.post("/api/v1/chat", json={"message": "Hello GraveyAI"})
    assert response.status_code == 200
    body = response.json()
    assert body["provider"] == "mock"
    assert "Hello GraveyAI" in body["response"]

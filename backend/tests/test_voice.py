from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_voice_transcribe_requires_authentication():
    response = client.post(
        "/api/v1/voice/transcribe",
        files={"audio": ("voice.wav", b"audio", "audio/wav")},
    )
    assert response.status_code == 401


def test_voice_transcribe_with_mock_provider():
    response = client.post(
        "/api/v1/voice/transcribe",
        headers={"Authorization": "Bearer development-token"},
        files={"audio": ("voice.wav", b"audio", "audio/wav")},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["provider"] == "mock-stt"
    assert body["language"] == "en"


def test_voice_respond_with_mock_providers():
    response = client.post(
        "/api/v1/voice/respond?language=sw",
        headers={"Authorization": "Bearer development-token"},
        files={"audio": ("voice.wav", b"audio", "audio/wav")},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["stt_provider"] == "mock-stt"
    assert body["tts_provider"] == "mock"
    assert body["language"] == "sw"

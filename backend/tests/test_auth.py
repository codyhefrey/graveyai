import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.auth.dependencies import extract_bearer_token
from app.main import app

client = TestClient(app)


def test_bearer_token_is_required():
    with pytest.raises(HTTPException) as exc:
        extract_bearer_token(None)
    assert exc.value.status_code == 401


def test_bearer_token_is_extracted_case_insensitively():
    assert extract_bearer_token("bearer example-token") == "example-token"


def test_invalid_development_token_is_rejected():
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer wrong-token"},
    )
    assert response.status_code == 401


def test_development_identity_is_returned_for_configured_token():
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer development-token"},
    )
    assert response.status_code == 200
    assert response.json()["subject"] == "dev:user"

import pytest
from fastapi import HTTPException

from app.auth.dependencies import require_bearer_token


def test_bearer_token_is_required():
    with pytest.raises(HTTPException) as exc:
        require_bearer_token(None)
    assert exc.value.status_code == 401


def test_bearer_token_is_extracted():
    assert require_bearer_token("Bearer example-token") == "example-token"

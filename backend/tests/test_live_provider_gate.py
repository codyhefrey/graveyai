import pytest
from fastapi import HTTPException

from app.api.v1.router import get_ai_provider
from app.core.config import Settings


def test_paid_provider_requires_launch_security_before_production():
    settings = Settings(
        ai_provider="openai",
        environment="production",
        openai_api_key="not-a-real-api-key",
    )
    with pytest.raises(HTTPException) as err:
        get_ai_provider(settings=settings)
    assert err.value.status_code == 503


def test_provider_without_local_key_fails_closed():
    settings = Settings(
        ai_provider="openai",
        environment="development",
        openai_api_key=None,
    )
    with pytest.raises(HTTPException) as err:
        get_ai_provider(settings=settings)
    assert err.value.status_code == 503

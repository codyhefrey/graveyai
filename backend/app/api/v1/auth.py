from fastapi import APIRouter, Depends

from app.auth.dependencies import require_bearer_token
from app.auth.mock_provider import MockIdentityProvider

router = APIRouter(prefix="/auth", tags=["auth"])
provider = MockIdentityProvider()


@router.get("/me")
async def get_current_identity(token: str = Depends(require_bearer_token)):
    identity = await provider.verify(token)
    return {"subject": identity.subject, "email": identity.email, "name": identity.name}

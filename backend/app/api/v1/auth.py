from fastapi import APIRouter, Depends

from app.auth.dependencies import require_identity
from app.auth.provider import Identity

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/me")
async def get_current_identity(identity: Identity = Depends(require_identity)):
    return {
        "subject": identity.subject,
        "email": identity.email,
        "name": identity.name,
    }

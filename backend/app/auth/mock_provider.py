from app.auth.provider import Identity, IdentityProvider


class MockIdentityProvider(IdentityProvider):
    """Development-only provider. Replace with a real OIDC verifier in production."""

    async def verify(self, token: str) -> Identity:
        return Identity(subject=f"dev:{token}", email=None, name="Development User")

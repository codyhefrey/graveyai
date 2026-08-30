from fastapi import FastAPI

app = FastAPI(
    title="GraveyAI API",
    version="0.1.0",
    description="Backend API for the GraveyAI platform.",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Return a lightweight service health response."""
    return {"status": "ok", "service": "graveyai-api"}

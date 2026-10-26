"""Local HTTP integration probes. This is a mock-provider demo, not a live AI test."""
from __future__ import annotations
import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen

API = "http://127.0.0.1:8000"
WEB = "http://127.0.0.1:3000"
PROD = "http://127.0.0.1:3001"


def probe(url, message):
    request = Request(url, data=json.dumps({"message": message}).encode("utf-8"),
                      method="POST", headers={"Content-Type": "application/json"})
    try:
        with urlopen(request, timeout=20) as response:
            return response.status, json.load(response), response.headers
    except HTTPError as exc:
        return exc.code, json.load(exc), exc.headers


def test_end_to_end():
    with urlopen(API + "/health", timeout=15) as response:
        assert json.load(response)["status"] == "ok"
    with urlopen(WEB, timeout=20) as response:
        assert response.status == 200

    status, data, headers = probe(WEB + "/api/chat", "Integration-test message")
    assert status == 200, (status, data)
    assert data["provider"] == "mock"
    assert data["mode"] == "local-development"
    assert "Integration-test message" in data["response"]
    assert "no-store" in headers.get("Cache-Control", "")
    for bad in ("", " " * 5, "a" * 2001):
        status, payload, _ = probe(WEB + "/api/chat", bad)
        assert status == 400, (bad[:12], status, payload)
    print("GraveyAI real local Next.js -> FastAPI HTTP round-trip passed (mock provider).")


def test_production_disabled():
    with urlopen(PROD, timeout=20) as response:
        assert response.status == 200
    status, data, _ = probe(PROD + "/api/chat", "Cannot use production demo")
    assert status == 503, (status, data)
    print("GraveyAI production chat endpoint correctly fails closed.")


if __name__ == "__main__":
    import sys
    if sys.argv[1:] == ["production"]:
        test_production_disabled()
    elif sys.argv[1:] == ["local"]:
        test_end_to_end()
    else:
        raise SystemExit("Run with 'production' or 'local'")

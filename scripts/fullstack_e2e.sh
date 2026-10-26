#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
backend_pid=""
web_pid=""
cleanup() {
  if [ -n "$web_pid" ]; then kill "$web_pid" 2>/dev/null || true; fi
  if [ -n "$backend_pid" ]; then kill "$backend_pid" 2>/dev/null || true; fi
}
trap cleanup EXIT
wait_http() {
  local url="$1"
  local ready=0
  for _ in $(seq 1 80); do
    if curl -fsS "$url" -o /dev/null; then ready=1; break; fi
    sleep 1
  done
  if [ "$ready" != "1" ]; then echo "FAILED: server did not become healthy at $url"; return 1; fi
}

(cd backend && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000) > /tmp/graveyai-backend-e2e.log 2>&1 &
backend_pid=$!
wait_http http://127.0.0.1:8000/health

# Production must NOT expose the anonymous development chat route.
(cd frontend && npm run start -- --hostname 127.0.0.1 --port 3001) > /tmp/graveyai-production-e2e.log 2>&1 &
web_pid=$!
wait_http http://127.0.0.1:3001/
python scripts/fullstack_probe.py production
kill "$web_pid" 2>/dev/null || true
wait "$web_pid" 2>/dev/null || true
web_pid=""

# Only the local Next.js development server may access the mock API.
(cd frontend && npm run dev -- --hostname 127.0.0.1 --port 3000) > /tmp/graveyai-development-e2e.log 2>&1 &
web_pid=$!
wait_http http://127.0.0.1:3000/
python scripts/fullstack_probe.py local

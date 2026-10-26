import { NextResponse } from "next/server";

export const runtime = "nodejs";

// Production is fail-closed: the demo endpoint cannot be exposed by accident.
export async function POST(request: Request) {
  if (process.env.NODE_ENV === "production") {
    return NextResponse.json({ error: "Demo chat is disabled in production." }, { status: 503 });
  }

  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "Expected a JSON request." }, { status: 400 });
  }
  if (typeof body !== "object" || !body || !("message" in body) ||
      typeof body.message !== "string" || !body.message.trim() || body.message.length > 2000) {
    return NextResponse.json({ error: "Please enter 1–2,000 characters." }, { status: 400 });
  }

  const upstream = process.env.GRAVEYAI_BACKEND_URL || "http://127.0.0.1:8000";
  try {
    const response = await fetch(new URL("/api/v1/chat", upstream), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: body.message }),
      signal: AbortSignal.timeout(12000),
      cache: "no-store",
    });
    if (!response.ok) {
      return NextResponse.json({ error: "The local GraveyAI backend could not respond." }, { status: 502 });
    }
    const data: unknown = await response.json();
    if (typeof data !== "object" || !data || !("response" in data) || typeof data.response !== "string") {
      return NextResponse.json({ error: "Unexpected backend response." }, { status: 502 });
    }
    // Do not misrepresent the deterministic mock provider as a trained AI.
    return NextResponse.json({
      response: data.response,
      provider: "provider" in data ? data.provider : "unknown",
      mode: "local-development",
      notice: "The default backend uses a deterministic mock provider, not a deployed AI model."
    }, { headers: { "Cache-Control": "no-store" } });
  } catch {
    return NextResponse.json({ error: "Local backend unavailable; start the Python API." }, { status: 502 });
  }
}

"use client";

import { useState, type FormEvent } from "react";

type Message = { role: "user" | "assistant"; text: string };
type Reply = { response?: string; provider?: string; error?: string };
const samples = [
  { title: "Evidence provenance", text: "Track the origin, timestamp and integrity digest of ingested documents. Provenance is not proof that source content is true." },
  { title: "Retrieval-augmented generation", text: "Search indexed documents for relevant passages, then cite retrieved evidence when producing a supported answer." },
  { title: "Provider boundaries", text: "Separating model providers from application contracts supports testing and allows controlled replacement." },
];

export default function Home() {
  const [panel, setPanel] = useState<"chat" | "knowledge">("chat");
  const [message, setMessage] = useState("");
  const [history, setHistory] = useState<Message[]>([]);
  const [query, setQuery] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  async function send(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const prompt = message.trim();
    if (!prompt || busy) return;
    setError("");
    setBusy(true);
    setHistory(previous => [...previous, { role: "user", text: prompt }]);
    setMessage("");
    try {
      const response = await fetch("/api/chat", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: prompt }),
      });
      const result: Reply = await response.json();
      if (!response.ok || !result.response) throw new Error(result.error || "Chat is unavailable.");
      setHistory(previous => [...previous, { role: "assistant", text: result.response! }]);
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "Could not contact the backend.");
    } finally {
      setBusy(false);
    }
  }

  const filtered = samples.filter(item =>
    (item.title + " " + item.text).toLowerCase().includes(query.trim().toLowerCase())
  );

  return (
    <main className="shell">
      <nav className="nav">
        <div className="brand"><span className="mark">G</span> GraveyAI</div>
        <span className="badge">LOCAL DEVELOPMENT PROTOTYPE</span>
      </nav>
      <section className="hero">
        <p className="eyebrow">INTELLIGENCE • KNOWLEDGE • TRUST</p>
        <h1>Knowledge you can <span>verify.</span></h1>
        <p className="lead">A working local conversation interface and sample knowledge explorer. The default backend is a deterministic mock, not a production AI assistant.</p>
        <div className="actions" role="group" aria-label="Choose a workspace">
          <button className={panel === "chat" ? "primary" : "secondary"} aria-pressed={panel === "chat"} onClick={() => setPanel("chat")}>Start a conversation</button>
          <button className={panel === "knowledge" ? "primary" : "secondary"} aria-pressed={panel === "knowledge"} onClick={() => setPanel("knowledge")}>Explore knowledge</button>
        </div>
      </section>
      {panel === "chat" ? (
        <section className="workspace" aria-label="Chat development workspace">
          <h2>Local conversation</h2>
          <p className="mode">Development mode: backend responses use the configured provider, initially a mock that echoes your message. No conversation persistence.</p>
          <div className="transcript" aria-live="polite">
            {history.length === 0 && <p className="empty">Ask a question to test the backend integration.</p>}
            {history.map((entry, i) => (
              <p className={entry.role === "user" ? "bubble user" : "bubble assistant"} key={i}>
                <strong>{entry.role === "user" ? "You" : "GraveyAI demo"}</strong>{entry.text}
              </p>
            ))}
          </div>
          <form onSubmit={send} className="chatForm">
            <label htmlFor="prompt">Your message</label>
            <textarea id="prompt" value={message} maxLength={2000} rows={3}
              onChange={event => setMessage(event.target.value)}
              placeholder="Ask about the project architecture…" />
            <div className="chatActions">
              <button className="primary" type="submit" disabled={busy || !message.trim()}>{busy ? "Sending…" : "Send message"}</button>
              <button className="secondary" type="button" onClick={() => {setHistory([]); setError("");}}>Clear session</button>
            </div>
          </form>
          {error && <p role="alert" className="error">{error}</p>}
        </section>
      ) : (
        <section className="workspace" aria-label="Sample knowledge explorer">
          <h2>Sample knowledge explorer</h2>
          <p className="mode">Local example cards, not a live search index. Authenticated document ingestion and RAG search remain separate backend capabilities.</p>
          <label htmlFor="search">Search sample topics</label>
          <input id="search" value={query} onChange={event => setQuery(event.target.value)} placeholder="Try: evidence" />
          <div className="sampleGrid">
            {filtered.map(item => <article key={item.title}><h3>{item.title}</h3><p>{item.text}</p></article>)}
            {!filtered.length && <p>No sample topics match your search.</p>}
          </div>
        </section>
      )}
      <footer>GraveyAI · Development prototype · Authentication, persistent chats and production AI not yet enabled</footer>
    </main>
  );
}

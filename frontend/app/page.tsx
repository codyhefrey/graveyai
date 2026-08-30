export default function Home() {
  return (
    <main className="shell">
      <nav className="nav">
        <div className="brand"><span className="mark">G</span> GraveyAI</div>
        <div className="badge">GRAVEYCHAIN • QUANTUM-READY</div>
      </nav>

      <section className="hero">
        <p className="eyebrow">INTELLIGENCE • KNOWLEDGE • TRUST</p>
        <h1>Knowledge you can<br /><span>verify.</span></h1>
        <p className="lead">GraveyAI combines conversational intelligence, retrieval-augmented knowledge, and cryptographic provenance through GraveyChain.</p>
        <div className="actions">
          <button className="primary">Start a conversation</button>
          <button className="secondary">Explore knowledge</button>
        </div>
      </section>

      <section className="cards">
        <article><strong>01</strong><h2>Ask</h2><p>Interact with an AI assistant built for clear, useful answers.</p></article>
        <article><strong>02</strong><h2>Retrieve</h2><p>Ground responses in indexed documents and trusted knowledge.</p></article>
        <article><strong>03</strong><h2>Verify</h2><p>Use cryptographic fingerprints and GraveyChain provenance to track knowledge integrity.</p></article>
      </section>

      <footer>GraveyAI · Phase 5 · Built for trustworthy AI</footer>
    </main>
  );
}

"use client";

import { useState } from "react";

const treasuryAddress = "0x2D1889afB908Ea14D061CF14E91B319c6aE17eC9";

type EthereumProvider = {
  request: (args: { method: string; params?: unknown[] }) => Promise<unknown>;
};

declare global {
  interface Window {
    ethereum?: EthereumProvider;
  }
}

export default function WalletPage() {
  const [address, setAddress] = useState<string | null>(null);
  const [status, setStatus] = useState("Not connected");

  async function connectWallet() {
    if (!window.ethereum) {
      setStatus("No EVM wallet detected. Install or open a compatible wallet.");
      return;
    }

    try {
      setStatus("Requesting wallet access…");
      const accounts = (await window.ethereum.request({
        method: "eth_requestAccounts",
      })) as string[];
      const connected = accounts?.[0];
      if (!connected) throw new Error("Wallet returned no account.");
      setAddress(connected);
      setStatus("Wallet connected. Payment verification is server-authoritative.");
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Wallet connection failed.");
    }
  }

  return (
    <main className="shell">
      <nav className="nav">
        <div className="brand"><span className="mark">G</span> GraveyAI</div>
        <div className="badge">NON-CUSTODIAL WALLET</div>
      </nav>

      <section className="hero">
        <p className="eyebrow">COMMERCIAL • WALLET • TRUST</p>
        <h1>Own your<br /><span>access.</span></h1>
        <p className="lead">
          Connect an EVM wallet to establish a wallet identity. GraveyAI never asks for or stores a seed phrase or private key.
        </p>
        <div className="actions">
          <button type="button" className="primary" onClick={connectWallet}>
            {address ? "Wallet connected" : "Connect wallet"}
          </button>
        </div>
        <p className="lead" style={{ marginTop: "1rem", fontSize: "0.9rem" }}>
          {status}
        </p>
      </section>

      <section className="cards">
        <article>
          <strong>TREASURY</strong>
          <h2>Receiving address</h2>
          <p style={{ wordBreak: "break-all" }}>{treasuryAddress}</p>
        </article>
        <article>
          <strong>AUTH</strong>
          <h2>Sign, don&apos;t share keys</h2>
          <p>Wallet ownership will be verified with a nonce-bound ERC-4361 Sign-In with Ethereum challenge.</p>
        </article>
        <article>
          <strong>PAYMENTS</strong>
          <h2>Verify on-chain</h2>
          <p>Commercial entitlements will only be activated after server-side transaction verification and idempotent reconciliation.</p>
        </article>
      </section>

      <footer>GraveyAI · Non-custodial commercial wallet layer</footer>
    </main>
  );
}

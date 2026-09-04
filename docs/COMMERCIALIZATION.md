# GraveyAI Commercialization & Wallet Architecture

## Objective

Turn GraveyAI into a commercially deployable AI platform while keeping ownership of funds non-custodial. GraveyAI should never require a private key or seed phrase from a user.

## Commercial model

### Free
- Basic AI assistance
- Limited research/RAG usage
- Public knowledge workflows
- Wallet connection

### Pro
- Higher usage limits
- Advanced research workflows
- Persistent personal memory
- Premium model routing
- Advanced provenance and export

### Research / Professional
- Larger context and knowledge bases
- Team workspaces
- API access
- Reproducible research runs
- Audit and provenance features

### Enterprise / Institutional
- Organization identity and RBAC
- Private knowledge infrastructure
- Dedicated deployments
- Policy controls
- Compliance and audit integrations
- Custom model/provider routing

## Revenue rails

The platform should support multiple payment rails rather than making cryptocurrency mandatory:

1. Conventional subscription/payment processing.
2. On-chain payments for supported networks/assets.
3. Enterprise invoicing.
4. API usage billing.
5. Research/institutional plans.
6. Future Gravey ecosystem credits or tokens only after separate legal, economic, security, and governance review.

## Wallet architecture

The wallet connection is **non-custodial**:

```text
User Wallet
    │
    │ connect / sign
    ▼
GraveyAI Web Client
    │
    │ wallet address + signed proof
    ▼
Wallet Verification API
    │
    ├── identity binding
    ├── payment authorization
    └── entitlement lookup
             │
             ▼
       GraveyAI Services
```

### Security rules

- Never request a seed phrase or private key.
- Never store private keys.
- Never ask users to paste a secret recovery phrase into GraveyAI.
- Transaction signing must happen inside the user's wallet.
- Server-side wallet ownership verification must use challenge/nonce signatures.
- Payment events must be independently verified on-chain before granting paid entitlements.
- Wallet addresses are identifiers, not authentication by themselves.
- Separate wallet identity from application identity so users can rotate wallets.

## Required production components

- Wallet adapter for the selected chain.
- Server-generated one-time nonce.
- Signature verification.
- Replay protection and nonce expiration.
- Chain/network allowlist.
- Payment intent and transaction tracking.
- On-chain confirmation policy.
- Idempotent payment processing.
- Subscription/entitlement ledger.
- Refund/dispute handling for off-chain payment rails.
- Compliance review before commercial launch in each target jurisdiction.

## Initial implementation boundary

The first implementation should be a wallet **connection and ownership-proof layer**, not a custodial wallet and not an unrestricted transaction executor.

The chain and asset should be configured explicitly. Do not hard-code a wallet address or private key into source control.

## Commercial readiness gates

A production launch requires:

- legal entity and terms;
- privacy policy;
- acceptable-use policy;
- billing and refund policy;
- tax treatment;
- security review;
- wallet/payment threat model;
- transaction monitoring;
- incident response;
- backups and recovery;
- observability;
- production identity and RBAC;
- rate limiting;
- financial reconciliation.

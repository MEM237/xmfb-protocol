## 🔧 XMFB Architecture Diagram

```
┌────────────────────────────┐
│ EscalatorPresenceAgent (A) │
│  - initiates ::μ~zen reflex│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│     GatekeeperAgent (B)    │
│  - receives reflex request │
│  - responds with sigil     │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│       TranscriptAgent       │
│  - if sigil is μ:μ or μ::   │
│    create %smash-tag        │
│  - append log to YAML chain │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│    smash_chain.yaml         │
│  - persists symbolic events │
│  - stores %smash-tag        │
│  - timestamp + sigil + IDs  │
└────────────────────────────┘
```

### 🧠 Summary:

* The `EscalatorPresenceAgent` initiates the presence challenge (`::μ~zen`).
* The `GatekeeperAgent` reflects back a symbolic sigil.
* If the sigil is "μ:μ" or "μ::", the `TranscriptAgent` issues a `%smash-tag` and logs it.
* The log is written to `chain/smash_chain.yaml` in YAML format, readable and portable.

Each agent is autonomous, connected only by intent and message.
This architecture models reflexive presence, trust, and logged verification in symbolic form.


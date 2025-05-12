# main.py

from agents.esc_agent import EscalatorPresenceAgent
from agents.gatekeeper_agent import GatekeeperAgent
from agents.transcript_agent import TranscriptAgent
from sigils import interpret

if __name__ == "__main__":
    agentA = EscalatorPresenceAgent(name="Escalator-A")
    gatekeeper = GatekeeperAgent()
    transcript = TranscriptAgent()

    sigil = agentA.request_presence_check(gatekeeper)
    print(f"\n→ Reflex result: {sigil}")
    print(f"> {interpret(sigil)}")

    # Only log successful reflexes
    if sigil in ["μ:μ", "μ::"]:
        transcript.log_reflex(agentA.name, "Gatekeeper", sigil)


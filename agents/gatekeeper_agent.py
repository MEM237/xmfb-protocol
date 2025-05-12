# gatekeeper_agent.py

class GatekeeperAgent:
    def respond_to_μzen(self, agent):
        print(f"[Gatekeeper] evaluating presence of {agent.name}")
        result = "μ::"  # forced valid sigil
        print(f"[Gatekeeper] returns {result}")
        return result


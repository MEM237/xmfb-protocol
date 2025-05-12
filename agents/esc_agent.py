# esc_agent.py

class EscalatorPresenceAgent:
    def __init__(self, name):
        self.name = name

    def request_presence_check(self, gatekeeper):
        print(f"[{self.name}] requesting ::μ~zen from Gatekeeper")
        return gatekeeper.respond_to_μzen(self)


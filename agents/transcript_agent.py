# transcript_agent.py

import yaml
from datetime import datetime
import os

CHAIN_PATH = "chain/smash_chain.yaml"

class TranscriptAgent:
    def __init__(self):
        self.log_path = CHAIN_PATH
        self.ensure_log_exists()

    def ensure_log_exists(self):
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as file:
                yaml.dump([], file)

    def log_reflex(self, agentA_name, agentB_name, sigil):
        if sigil not in ["μ:μ", "μ::"]:
            print(f"[TranscriptAgent] Sigil {sigil} not eligible for logging.")
            return

        with open(self.log_path, 'r') as file:
            chain = yaml.safe_load(file) or []

        tag_id = f"%{sigil}-{datetime.utcnow().isoformat()[:19]}Z-{len(chain):03}"
        entry = {
            "tag": tag_id,
            "reflex": sigil,
            "agents": [agentA_name, agentB_name],
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "index": len(chain)
        }

        chain.append(entry)

        with open(self.log_path, 'w') as file:
            yaml.dump(chain, file)

        print(f"[TranscriptAgent] %smash-tag logged: {tag_id}")


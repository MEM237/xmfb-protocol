# sigils.py

SIGIL_CODES = {
    "μ:μ": "mutual presence confirmed",
    "μ::": "presence verified and trusted",
    ":μ:": "half-reflection (incomplete trust)",
    "x~x": "reflex failed (mirror broken)",
    "~ ~": "no response / ghost presence",
    "μ~!": "distorted reflection",
    ":~:": "loopback detected (self-reflection)",
    "!!!": "emergency denial",
    ":?~": "temporal desync / unclear presence"
}

def interpret(code):
    return SIGIL_CODES.get(code, "unknown sigil")

def is_valid(code):
    return code in SIGIL_CODES

if __name__ == "__main__":
    codes = ["μ:μ", ":μ:", "x~x", "~ ~", "μ~!", ":~:", "!!!", ":?~", 
"???"]
    for code in codes:
        print(f"{code} → {interpret(code)}")


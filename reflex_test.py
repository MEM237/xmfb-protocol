# reflex_test.py

from sigils import interpret

def simulate_reflex(reflex_code):
    print(f"Testing reflex code: {reflex_code}")
    print(f"→ {interpret(reflex_code)}\n")

if __name__ == "__main__":
    test_codes = ["μ:μ", "μ::", ":μ:", "x~x", "~ ~", "μ~!", ":~:", "!!!", 
":?~", "???"]
    for code in test_codes:
        simulate_reflex(code)


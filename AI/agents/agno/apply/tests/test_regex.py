
import re

def preprocess(expression):
    return re.sub(r'\b([eE])(\d+)\b', r'1\1\2', expression)

test_cases = [
    "e5",
    "1e5",
    "1.2e5",
    "e-5",
    "e+5",
    "E10",
    "2 + e5",
    "(e5)",
    "exp(5)",
    "ae5",
    "e5*2"
]

for tc in test_cases:
    print(f"'{tc}' -> '{preprocess(tc)}'")

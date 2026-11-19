import re
pattern = r"[A-Z]+arth"

text = "arth is a common suffix in words like Earth, Hearth, and Farth."
matches = re.finditer(pattern, text)

for match in matches:
    print(f"Match found: {match.group()}")
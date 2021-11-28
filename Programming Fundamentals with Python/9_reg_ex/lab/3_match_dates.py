import re

text = input()
pattern = r"((\d{2})([/\.-])([A-Z][a-z]{2})\2(\d){4})"
matches = re.finditer(pattern, text)
for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")

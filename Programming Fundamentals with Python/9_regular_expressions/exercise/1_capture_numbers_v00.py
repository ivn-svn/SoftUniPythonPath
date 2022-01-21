import re
pattern = r"(([1-9][0-9]*)|0$)"

user_input = input()
matches = re.finditer(pattern, user_input)


for match in matches:
    print(match.group(0), end=" ")
# https://judge.softuni.org/Contests/Practice/Index/2302#1
import re

pattern = r"(\d+)"
user_input = "test"
output = ""
while user_input != "":
    user_input = input()

    matches = re.finditer(pattern, user_input)

    for match in matches:
        output += match.group(0) + " "


print(output)

# regex to use:
# (?<=::)([A-Z][a-z][a-z]+)(?=::)|(?<=\*\*)([A-Z][a-z][a-z]+)(?=\*\*)
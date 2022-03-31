# https://judge.softuni.org/Contests/1743
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
#
# pattern = r""
# user_input = input()
# while user_input != "":
#     user_input = input()

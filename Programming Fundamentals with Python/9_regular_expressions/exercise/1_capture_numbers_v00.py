import re
pattern = r"(([1-9][0-9]*)|0$)"
matches = []
user_input = input()
while user_input != '':
    matches += re.findall(pattern, user_input)
    user_input = input()


for match in matches:

    print(match, end=" ")
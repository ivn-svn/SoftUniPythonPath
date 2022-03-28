# import re
# user_input = input()
# pattern = r"(\w+(|\-|\.|\_)@\w+(\-|\.|\_)\.\w+)"
# matches = re.findall(pattern, user_input)
# print(matches)
#
import re
user_input = input()

pattern = r"(\b\S+@\S+\b)"

matches = re.findall(pattern, user_input)
for match in matches:
    print(match, end="\n")

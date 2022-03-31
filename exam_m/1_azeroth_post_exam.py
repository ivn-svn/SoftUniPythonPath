import re
data_input = input()
pattern = r"(\b[A-Z][a-z]*)\s(\b[A-Z][a-z]*)"
command = re.findall(pattern, data_input)
for x in command:
    print(x)
print(command)
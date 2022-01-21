# Source: https://softuni.bg/forum/answers/details/65976

data = input()
output = ""
bomb = 0

for i in range(len(data)):
    if data[i] == ">":
        bomb += int(data[i + 1])
        output += data[i]
    elif data[i] != ">" and bomb > 0:
        bomb -= 1
    else:
        output += data[i]

print(output)
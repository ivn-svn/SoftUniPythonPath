from collections import deque

# The game starts with 0 collected hazelnuts. Your goal is to collect 3 of them.
# You get as input the size of the field, which will be always a square shape. 
# After that, you will receive the commands with directions in which the squirrel can move:
# "left", "right", "down", and "up" in a sequence, each value separated by a comma and a space (", "). 
# e.g. input:

# On the next rows, you will receive the field.
# rows = ["**h**", "t****", "*h***", "*h*s*", "*****"]


gameon = True
out = False

n = int(input())
matrix = []
commands =  deque(input().split(", "))
# commands = deque("left, left, up, right, up, up".split(", "))
for line in range(n):
    rows = list(input())
    matrix.append(rows)
trapped = False
# rows = ["**h**", "t****", "*h***", "*h*s*", "*****"]

for row in rows:
    matrix.append(list(row))

hazelnuts_count = 0

def locateSquirrel(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            square = matrix[i][j]
            if square == "s":
                return i, j
    return None


def locateHazelnut(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            square = matrix[i][j]
            if square == "h":
                return i, j
    return None


def moveSquirrel(old_pos, command, matrix, gameon, out):
    new_pos = old_pos
    if command  == "left":
        if old_pos[1] - 1 < 0:
            print("The squirrel is out of the field.")
            out = True
            gameon = False
        else:
            new_pos[1] = old_pos[1] - 1
    elif command == "right":
        if old_pos[1] + 1 >= n:
            print("The squirrel is out of the field.")
            out = True
            gameon = False
        else:
            new_pos[1] = old_pos[1] + 1
    elif command == "down":
        if old_pos[0] + 1 >= n:
            print("The squirrel is out of the field.")
            out = True
            gameon = False
        else:
            new_pos[0] = old_pos[0] + 1
    elif command == "up":
        if old_pos[0] - 1 < 0:
            print("The squirrel is out of the field.")
            out = True
            gameon = False
        else:
            new_pos[0] = old_pos[0] - 1
    return old_pos, matrix, new_pos, gameon, out

old_pos = list(locateSquirrel(matrix))

while commands and gameon:
    command = commands.popleft()
    old_pos, matrix, new_pos, gameon, out = moveSquirrel(old_pos, command, matrix, gameon, out)
    if gameon: 
            
        sq = matrix[new_pos[0]][new_pos[1]]

        if sq == "h":
            hazelnuts_count += 1
            matrix[new_pos[0]][new_pos[1]] = "s"
            matrix[old_pos[0]][old_pos[1]] = "*"
           # print(f"Hazelnut found at ({new_pos[0]}, {new_pos[1]})")
        elif sq == "*":
            matrix[old_pos[0]][old_pos[1]] = "*"
            matrix[new_pos[0]][new_pos[1]] = "s"
        elif sq == "t":
            trapped = True
           # print(f"Trap found at ({new_pos[0]}, {new_pos[1]})")
            print("Unfortunately, the squirrel stepped on a trap...")
            matrix[old_pos[0]][old_pos[1]] = "*"
            gameon = False
            break
        if hazelnuts_count >= 3:
            gameon = False
            break
    else:
        break

if hazelnuts_count == 3:  
    print("Good job! You have collected all hazelnuts!")
else:
    if not trapped and not out:
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_count}")

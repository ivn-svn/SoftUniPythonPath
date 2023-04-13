from collections import deque


def locatePawns(rows):
    for row in range(len(rows) - 1, -1, -1):
        squares = rows[row]
        for square in range(len(squares) - 1, -1, -1):
            if squares[square] == "b":
                black = [row, square]
            elif squares[square] == "w":
                white = [row, square]
    return white, black            

gameon = True
# n = 5
# commands = deque("left, left, up, right, up, up".split(", "))
# rows = ["**h**", "t****", "*h***", "*h*s*", "*****"]
matrix = []
hazelnuts_count = 0

# s - represents the squirrel's position.
# h – represents a hazelnut. 
# * – the asterisk represents an empty position.
# t – represents a trap.

n = int(input())
commands =  deque(input().split(", "))
for line in range(n):
    rows = input()
    matrix.append(rows)



# for row in rows:
#     matrix.append(row)

hazelnuts_count = 0

def moveSquirrel(old_posSquirrel, command, matrix, gameon):
    old_posSquirrel = old_posSquirrel
    new_posSquirrel = old_posSquirrel
    if command  == "left":
        if old_posSquirrel[1] - 1 < 0:
            print("The squirrel is out of the field.")
            gameon = False
        else:
            new_posSquirrel[1] = old_posSquirrel[1] - 1
    elif command == "right":
        if old_posSquirrel[1] + 1 > n:
            print("The squirrel is out of the field.")
            gameon = False
        else:
            new_posSquirrel[1] = old_posSquirrel[1] + 1
    elif command == "down":
        if old_posSquirrel[0] + 1 > n:
            print("The squirrel is out of the field.")
            gameon = False
        else:
            new_posSquirrel = old_posSquirrel[0] + 1
    elif command == "up":
        if old_posSquirrel[0] - 1 < 0:
            print("The squirrel is out of the field.")
            gameon = False
        else:
            new_posSquirrel[0] = old_posSquirrel[0] - 1
    return list(old_posSquirrel), matrix, list(new_posSquirrel), gameon


def locateSquirrel(matrix):
    for i, row in enumerate(matrix):
        for j, square in enumerate(row):
            if square == "s":
                return i, j
    return None


def locateHazelnut(matrix):
    for i, row in enumerate(matrix):
        for j, square in enumerate(row):
            if square == "s":
                return list(i, j)
    return None


while commands and gameon:
    command = commands.popleft()
    pos = locateSquirrel(matrix)
    pos, matrix, new_pos, gameon = moveSquirrel(pos, command, matrix, gameon)
    sq = matrix[pos[0]][pos[1]]
    if sq == "h":
        hazelnuts_count += 1
        matrix[pos[0]][pos[1]] = "*"
        print(f"Hazelnut found at ({pos[0]}, {pos[1]})")
    elif sq == "*":
        matrix[pos[0]][pos[1]] = "s"
    elif sq == "t":
        print(f"Trap found at ({pos[0]}, {pos[1]})")
        gameon = False
        break
    if hazelnuts_count >= 3:
        break


if not locateHazelnut(matrix):  
    print("Good job! You have collected all hazelnuts!")
else:
    print("There are more hazelnuts to collect.")


print(f"Hazelnuts collected: {hazelnuts_count}")
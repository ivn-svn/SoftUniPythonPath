import copy
from collections import deque

inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])  #  matrix dimensions
# n, m = 4, 4 #  matrix dimensions

touches_c = 0
moves_c = 0
rows = []
for count in range(n):
    row = input()
    rows.append(row)
# row = input().split(" ")
# matrix = ("""O B O -\n- P O P\n- - P -\n- - - -""".split("\n"))
# rows = ["O B O -", "- P O P", "- - P -", "- - - -"]
# matrix = """O B O -\n- P O P\n- - P -\n- - - -""" 
# matrix = rows.split(" ")
matrix = list()
for row in rows:
    row = row.split(" ")
    matrix.append(row)

def printBattlefield(battlefield):
    drawn = ""
    for row in battlefield:
        for square in row:
            drawn += square
        drawn += "\n"    
    drawn.strip()
    return drawn


def validatePosition(n, m, pos):
    if pos[0] >= 0 and pos[0] < n and pos[1] < m and pos[1] >= 0: 
        return pos
    else:
        return None


def locatePlayer(matrix):
    idx_row = 0
    idx_square = 0
    positions = []
    for row in matrix:
        idx_square = 0
        for square in row:
            if square == "B":
                positions = [idx_row, idx_square]
                return positions
            idx_square += 1
        idx_row += 1
    return None


def movePlayer(matrix, new_player_pos, old_player_pos, touches_c, moves_c):
    square = matrix[new_player_pos[0]][new_player_pos[1]]
    if square == "O":
        pass
    elif square == "P":
        matrix[new_player_pos[0]][new_player_pos[1]] = "B"
        matrix[old_player_pos[0]][old_player_pos[1]] = "-"
        touches_c += 1
        moves_c += 1
    elif square == "-":
        matrix[new_player_pos[0]][new_player_pos[1]] = "B"
        matrix[old_player_pos[0]][old_player_pos[1]] = "-"
        moves_c += 1
    return matrix, touches_c, moves_c



#commands = deque(["left", "right", "down", "right", "down", "right", "up", "right", "up", "down", "Finish"])
#command = commands.popleft()
command = ""
while command != "Finish": 
    command = input()

    if command == "Finish":
        break
    player_pos = locatePlayer(matrix)
    old_player_pos = player_pos
    new_player_pos = copy.deepcopy(player_pos)
    if command == "left":
        old_player_pos[1] = player_pos[1]
        new_player_pos[1] = player_pos[1] - 1
        new_player_pos = validatePosition(n, m, new_player_pos)

    elif command == "right":
        old_player_pos[1] = player_pos[1]
        new_player_pos[1] = player_pos[1] + 1
        new_player_pos = validatePosition(n, m, new_player_pos)

    elif command == "down":
        old_player_pos[0] = player_pos[0]
        new_player_pos[0] = player_pos[0] + 1
        new_player_pos = validatePosition(n, m, new_player_pos)

    elif command == "up":
        old_player_pos[0] = player_pos[0]
        new_player_pos[0] = player_pos[0] - 1
        new_player_pos = validatePosition(n, m, new_player_pos)

    if new_player_pos is not None:
        matrix, touches_c, moves_c = movePlayer(matrix, new_player_pos, old_player_pos, touches_c, moves_c)  

    # print(printBattlefield(matrix)) 

    # command = commands.popleft() # To be removed 


print("Game over!")
print(f"Touched opponents: {touches_c} Moves made: {moves_c}")

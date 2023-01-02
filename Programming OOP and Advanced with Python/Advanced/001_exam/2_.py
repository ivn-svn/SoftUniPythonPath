def coordsOf(matrix, searchable):
    pos = [0, 0]
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            current_item = matrix[row][col]
            #print(current_item)
            if current_item == searchable:
                pos = [row, col]
    return pos


def matrixMoveSubmarine(move, row, col):
    if move == "right":
        col += 1
    elif move == "left":
        col -= 1
    elif move == "up":
        row -= 1
    elif move == "down":
        row += 1
    return row, col


def battlefieldUpdate(old_positions, new_positions, matrix, destroyed_ships, u9_hits):
    row_old = old_positions[0]
    col_old = old_positions[1]
    row_new = new_positions[0]
    col_new = new_positions[1]

    if matrix[row_new][col_new] == "C":
        destroyed_ships += 1
    elif matrix[row_new][col_new] == "*":
        u9_hits += 1

    matrix[row_old][col_old] = "-"
    matrix[row_new][col_new] = "S"
    return matrix, destroyed_ships, u9_hits


def printFunc(matrix):
    for print_row in matrix:
        print("".join(print_row))

rows = list()
game_on = True
n = int(input())

for i in range(n):
    rows.append(list(input()))

destroyed_ships = 0
u9_hits = 0

while game_on:

    nazi_pos = coordsOf(rows, "S")
    # print(nazi_pos)
    brit_pos = coordsOf(rows, "C")
    # print(brit_pos)
    mine_pos = coordsOf(rows, "*")
    # print(mine_pos)

    nazi_row, nazi_col = nazi_pos[0], nazi_pos[1]
    brit_row, brit_col = brit_pos[0], brit_pos[1]
    mine_row, mine_col = mine_pos[0], mine_pos[1]


    if u9_hits >= 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{nazi_row}, {nazi_col}]!")
        printFunc(rows)
        game_on = False

    elif destroyed_ships >= 3:
        print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        printFunc(rows)
        game_on = False

    else:
        move = input()
        old_nazi_pos = [nazi_row, nazi_col]
        new_nazi_pos = matrixMoveSubmarine(move, nazi_row, nazi_col)
        rows, destroyed_ships, u9_hits = battlefieldUpdate(old_nazi_pos, new_nazi_pos, rows, destroyed_ships, u9_hits)



    # print("\n")
    # print(f"Ships destroyed: \n{destroyed_ships}")
    # print(f"U9 hits: \n{u9_hits}")
    # print("\n")

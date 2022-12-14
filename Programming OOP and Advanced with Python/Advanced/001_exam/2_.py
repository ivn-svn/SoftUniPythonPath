def coordsOf(matrix, searchable):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            current_row = matrix[row]
            current_item = matrix[row][col]
            if matrix[row][col] == searchable:
                pos = [row, col]
                return pos


def matrixMoveSubmarine(move, row, col):
    if move == "right":
        col += 1
    elif move == "left":
        col -= 1
    elif move == "up":
        row += 1
    elif move == "down":
        row -= 1
    return row, col


def battlefieldUpdate(old_positions, new_positions, matrix):
    row_old = old_positions[0]
    col_old = old_positions[1]
    row_new = new_positions[0]
    col_new = new_positions[1]
    matrix[row_old][col_old] = "-"
    matrix[row_new][col_new] = "S"
    return matrix


rows = list()
game_on = True
n = int(input())

for i in range(n):
    rows.append(list(input()))

destroyed_ships = 0
u9_hits = 0

while game_on and u9_hits < 3 and destroyed_ships < 3:

    nazi_pos = coordsOf(rows, "S")
    brit_pos = coordsOf(rows, "C")
    mine_pos = coordsOf(rows, "*")

    nazi_row, nazi_col = nazi_pos[0], nazi_pos[1]
    brit_row, brit_col = brit_pos[0], brit_pos[1]
    mine_row, mine_col = mine_pos[0], mine_pos[1]

    if nazi_pos == brit_pos and destroyed_ships < 3:
        destroyed_ships += 1
        rows = battlefieldUpdate(nazi_pos, brit_pos, rows)

    elif nazi_pos == mine_pos and u9_hits < 3:
        u9_hits += 1
        rows = battlefieldUpdate(nazi_pos, mine_pos, rows)

    if u9_hits >= 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{nazi_pos[0]}, {nazi_pos[1]}]!")
        game_on = False
        break
    elif destroyed_ships >= 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        game_on = False
        break
    move = input()
    old_nazi_pos = [nazi_row, nazi_col]
    new_nazi_pos = matrixMoveSubmarine(move, nazi_row, nazi_col)
    rows = battlefieldUpdate(old_nazi_pos, new_nazi_pos, rows)

for print_row in rows:
    print("".join(print_row))

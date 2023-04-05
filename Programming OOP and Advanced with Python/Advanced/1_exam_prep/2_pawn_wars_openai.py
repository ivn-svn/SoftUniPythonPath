from collections import deque

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

coords_matrix = []
coords_row = []
for row in range(8, 0, -1):
    for letter in letters:
        coords_row.append(f"{letter}{row}")
    #    print(f" {letter}{row} ", end="") 
    coords_matrix.append(coords_row)
   # print("\n")


matrix = """- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -"""

# matrix = """- - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - b - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -"""

matrix = [[sq for sq in r.split(" ")] for r in matrix.split("\n")]


def locatePawns(rows):
    for row in range(len(rows) - 1, -1, -1):
        squares = rows[row]
        for square in range(len(squares) - 1, -1, -1):
            if squares[square] == "b":
                black = [row, square]
            elif squares[square] == "w":
                white = [row, square]
    return white, black, matrix            


def capturePawn(matrix, turn):
    white, black, matrix = locatePawns(matrix)
    pawn_capture = False
    if (white[0] +1) == black[0] or (white[0] -1) == black[0]:
        if (white[1] +1) == black[1] or (white[1] -1) == black[1]:
            pawn_capture = True
            if turn == "white":
                print(f"Game over! {turn} win, capture on {black[0]}, {black[1]}.")
            elif turn == "black":
                print(f"Game over! {turn} win, capture on {white[0]}, {white[1]}.")
    return pawn_capture, turn
    

def movePawns(white, black, matrix, turn):
    matrix[white[0]][white[1]] = '-'
    matrix[black[0]][black[1]] = '-'
    white, black, matrix = locatePawns(matrix)
    game_on = True
    if white[0] == 0:
        game_on = False
        player = "white"
        print(f"Game over! {player} pawn is promoted to a queen at {coords_matrix[white[0]][white[1]]}. {white[0]} {white[1]}")
    elif black[0] == 7:
        game_on = False
        player = "black"
        print(f"Game over! {player} pawn is promoted to a queen at {coords_matrix[black[0]][black[1]]}. {black[0]}{black[1]}")
    else:
        if turn == "white":
            white[0] = white[0] - 1
            turn = "black"
        else:
            black[0] = black[0] + 1
            turn = "white"
        matrix[white[0]][white[1]] = 'w'
        matrix[black[0]][black[1]] = 'b'
        matrix = printMatrix(matrix)
        print(matrix)
    return matrix, game_on, white, black, turn


def printMatrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()


white, black, matrix = locatePawns(matrix)

game_on = True
turn = "white"
while game_on:
    capture, turn = capturePawn(matrix, turn)
    white, black, matrix = locatePawns(matrix)

    if game_on:
        if capture:
            game_on = False
            break
        else:
            matrix, game_on, white, black, turn = movePawns(white, black, matrix, turn)
        printMatrix(matrix)
    else: 
        break
 

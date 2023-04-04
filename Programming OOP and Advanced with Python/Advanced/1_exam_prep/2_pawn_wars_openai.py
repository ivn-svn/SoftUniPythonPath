from collections import deque

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

coords_matrix = []
coords_row = []
for row in range(8, 0, -1):
    for letter in letters:
        coords_row.append(f"{letter}{row}")
        print(f" {letter}{row} ", end="") 
    coords_matrix.append(coords_row)
    print("\n")


matrix = """- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -"""

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

def movePawns(white, black, matrix):
    matrix[white[0]][white[1]] = '-'
    matrix[black[0]][black[1]] = '-'

    if white[0] == 0:
        game_on = False
        player = "white"
        print(f"Game over! {player} pawn is promoted to a queen at {coords_matrix[white[0]][white[1]]}.")
        return matrix, game_on, white, black

    elif black[0] == 7:
        game_on = False
        player = "black"
        print(f"Game over! {player} pawn is promoted to a queen at {coords_matrix[black[0]][black[1]]}.")
        return matrix, game_on, white, black

    else:
        white[0] -= 1
        black[0] += 1
        matrix[white[0]][white[1]] = 'w'
        matrix[black[0]][black[1]] = 'b'
        game_on = True
        return matrix, game_on, white, black

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()

white, black, matrix = locatePawns(matrix)

game_on = True

while game_on:
    if game_on:
        printMatrix(matrix)
    else: 
        break
    white, black, matrix = locatePawns(matrix)
    matrix, game_on, white, black = movePawns(white, black, matrix)
 

printMatrix(matrix)

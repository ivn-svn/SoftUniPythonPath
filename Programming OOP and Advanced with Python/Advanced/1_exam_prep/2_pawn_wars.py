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
    if white[0] == 0:
        game_on = False
        square = white
        player = "white"
        print(f"Game over! {player} pawn is promoted to a queen at {square}.")
        print(game_on)
        return matrix, game_on, white, black

    elif black[0] == 7:
        game_on = False
        square = black
        player = "black"
        print(f"Game over! {player} pawn is promoted to a queen at {square}.")
        print(game_on)
        return matrix, game_on, white, black

    else:
        white[0] = white[0] + 1
        black[0] = black[0] - 1

        print(white[0])
        print(black[0])
        game_on = True
        return matrix, game_on, white, black


def buildNewMatrix(matrix):
    matrix = "\n".join(["".join([square for square in row]) for row in matrix])
    return matrix


player = ""
square = ""

white, black, matrix = locatePawns(matrix)

game_on = True

while game_on:
    white, black, matrix = locatePawns(matrix)
    if white[0] == 0:
        game_on = False
        square = white
        player = "white"
        print(f"Game over! {player} pawn is promoted to a queen at {square}.")
        print(game_on)

    elif black[0] == 7:
        game_on = False
        square = black
        player = "black"
        print(f"Game over! {player} pawn is promoted to a queen at {square}.")
        print(game_on)

    else:
        white[0] = white[0] + 1
        black[0] = black[0] - 1

        print(white[0])
        print(black[0])
        game_on = True
    matrix, game_on, white, black = movePawns(white, black, matrix)
    matrix = buildNewMatrix(matrix)
    print(matrix)

print(black)
print(white)
print(matrix)


# Print either one of the following:
# If a pawn captures the other, print:
# print(f"Game over! {player} win, capture on {square}.")
# If a pawn reaches the last rank, print:
# print(f"Game over! {player} pawn is promoted to a queen at {square}.")

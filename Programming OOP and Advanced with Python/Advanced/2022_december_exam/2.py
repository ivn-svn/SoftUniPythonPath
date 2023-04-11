from collections import deque

n = int(input())
dnf = input()
input_for_comment = []
#input_for_comment = [". . . . .", ". . . T .", ". . . . .", ". T . . .", ". . F . ."]
for k in range(n):
    inp = input()
    input_for_comment.append(inp)
    
matrix = []
covered = 0
final = False
# commands = deque(["down", "right", "right", "right", "down", "right", "up", "down", "right", "up", "End"])

def printRacetrack(matrix):
    drawn = ""
    for row in range(n):
        line = "".join(matrix[row])
        if row < (n):
            drawn += "\n"
        drawn += line
    return drawn

def findTunel(matrix):
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "T":
                return (row, col)
    return None

for row in input_for_comment:
    row = row.split(" ")
    matrix.append(row)

# Initialize the generator
row, col = 0,0 
command = ""
while command != "End":
    command = input()
    # command = commands.popleft()

    if command == "down":
        if 0 <= row + 1 < n:
            row += 1
    elif command == "up":
        if 0 <= row - 1 < n:
            row -= 1
    elif command == "right":
        if 0  <= col +1 < n:
            col += 1
    elif command == "left":
        if 0 <= col -1 < n:
            col -= 1

    if matrix[row][col] == "T":
        matrix[row][col] = "."
        covered += 30
        row, col = findTunel(matrix)
        # if row != None and col != None: 
        #     matrix[row][col] = "."
        matrix[row][col] = "."

    elif matrix[row][col] == "F":
        matrix[row][col] = "C"
        covered += 10
        print(f"Racing car {dnf} finished the stage!")
        final = True
        break
    else:
        matrix[row][col] = "."
        covered += 10
    
    #matrix[row][col] = "1"

    # output = printRacetrack(matrix)
    # print(output)

    # Get the next position
#matrix[row][col] = "C"
if not final:
    print(f"Racing car {dnf} DNF.")

output = printRacetrack(matrix)
# print(covered)
print(f"Distance covered {covered} km. {output}")

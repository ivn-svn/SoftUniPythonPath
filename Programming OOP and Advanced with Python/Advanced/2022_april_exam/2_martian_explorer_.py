from collections import deque

def moveRover(old_pos_rover, command, rows):
    old_pos_rover = list(old_pos_rover)
    if command  == "left":
        if old_pos_rover[1] - 1 < 0:
            old_pos_rover[1] = 5
        else:
            old_pos_rover[1] -= 1
    elif command == "right":
        if old_pos_rover[1] + 1 > 5:
            old_pos_rover[1] = 0
        else:
            old_pos_rover[1] += 1
    elif command == "down":
        if old_pos_rover[0] + 1 > 5:
            old_pos_rover[0] = 0
        else:
            old_pos_rover[0] += 1
    elif command == "up":
        if old_pos_rover[0] - 1 < 0:
            old_pos_rover[0] = 5
        else:
            old_pos_rover[0] -= 1
    return tuple(old_pos_rover), rows


def locateRover(mars):
    for i, row in enumerate(mars):
        for j, square in enumerate(row):
            if square == "E":
                return (i, j)
    return None


water, metal, concrete = False, False, False
rows = []
for i in range(6):
    row = input().split()
    rows.append(row)

commands = deque(input().split(", "))
pos = locateRover(rows)

while commands:
    command = commands.popleft()
    pos, rows = moveRover(pos, command, rows)
    sq = rows[pos[0]][pos[1]]
    if sq == "W":
        water = True
        print(f"Water deposit found at ({pos[0]}, {pos[1]})")
    elif sq == "M":
        metal = True
        print(f"Metal deposit found at ({pos[0]}, {pos[1]})")
    elif sq == "C":
        concrete = True
        print(f"Concrete deposit found at ({pos[0]}, {pos[1]})")
    elif sq == "R":
        print(f"Rover got broken at ({pos[0]}, {pos[1]})")
        break

if water and metal and concrete:
    print("Area suitable to start the colony.")
else: 
    print("Area not suitable to start the colony.")

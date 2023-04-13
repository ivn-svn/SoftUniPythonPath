from collections import deque

def moveRover(old_pos_rover, command, rows):
    if command  == "left":
        if old_pos_rover[1] -1 < 0:
            
            old_pos_rover[1] = 5
            new_pos_rover = [old_pos_rover[0], old_pos_rover[1]]
        else:
            
            new_pos_rover = [old_pos_rover[0], old_pos_rover[1] -1]
    elif command == "right":
        if old_pos_rover[1] -1 > 5:
            
            old_pos_rover[1] = 0
            new_pos_rover = [old_pos_rover[0], old_pos_rover[1]]
        else:
            
            new_pos_rover = [old_pos_rover[0], old_pos_rover[1] +1]
    elif command == "down":
        if old_pos_rover[0] +1 > 5:
            
            old_pos_rover[0] = 0
            new_pos_rover = [old_pos_rover[0], old_pos_rover[1]]
        else:
            
            new_pos_rover = [old_pos_rover[0] +1, old_pos_rover[1]]    
    elif command == "up":
        if old_pos_rover[0] -1 < 0:
            
            old_pos_rover[0] = 0
            new_pos_rover = [old_pos_rover[0], old_pos_rover[1]]
        else:
            
            new_pos_rover = [old_pos_rover[0] -1, old_pos_rover[1]]    
    return new_pos_rover, rows


def locateRover(mars):
    idx_row = 0
    idx_square = 0
    pos_rover = []
    for row in mars:
        idx_square = 0
        for square in row:
            if square == "E":
                pos_rover = [idx_row, idx_square]
                return pos_rover
            idx_square += 1
        idx_row += 1
    return None


water, metal, concrete = False, False, False
rows = []
# r = ["- R - - - -", "- - - - - R", "- E - R - -", "- W - - - -", "- - - C - -", "M - - - - -"]
for i in range(6):
   # row = r[i]
    row = input()
    rows.append(row.split(" "))
    # rows.append(row)

# commands = deque(input().split(", "))
#commands = deque("down, right, down, right, down, left, left, left".split(", "))
running = True
pos = locateRover(rows)

commands = deque(input().split(", "))
while running and commands:
    command = commands.popleft()
    pos, rows = moveRover(pos, command, rows)
    sq = rows[pos[0]][pos[1]]
    if sq == "W": # Water deposit
        water = True
        print(f"Water deposit found at ({pos[0]}, {pos[1]})")
    elif sq == "M": # Metal deposit
        metal = True
        print(f"Metal deposit found at ({pos[0]}, {pos[1]})")
    elif sq == "C": # Concrete deposit
        concrete = True
        print(f"Concrete deposit found at ({pos[0]}, {pos[1]})")
    elif sq == "R": # Rock
        print(f"Rover got broken at ({pos[0]}, {pos[1]})")
        running = False
        break

if water and metal and concrete:
    print("Area suitable to start the colony.")
else: 
    print("Area not suitable to start the colony.")

n = int(input()) # Size of the matrix
battlefield = [] # The Matrix
destroyed = 0
hit_by_mine = 0 


def locateSubmarine(battlefield):
    idx_row = 0
    idx_square = 0
    pos_submarine = []
    for row in battlefield:
        idx_square = 0
        for square in row:
            if square == "S":
                pos_submarine = [idx_row, idx_square]
                return pos_submarine
            idx_square += 1
        idx_row += 1
    return None


def moveSubmarine(old_pos_submarine, command):
    if command  == "left":
        new_pos_submarine = [old_pos_submarine[0], old_pos_submarine[1] -1]
    elif command == "right":
        new_pos_submarine = [old_pos_submarine[0], old_pos_submarine[1] +1]
    elif command == "down":
        new_pos_submarine = [old_pos_submarine[0] +1, old_pos_submarine[1]]
    elif command == "up":
        new_pos_submarine = [old_pos_submarine[0] -1, old_pos_submarine[1]]
    return new_pos_submarine


def updateBattlefield(old_pos_sub, command, game_on, hit_by_mine, destroyed):
    new_pos_sub = moveSubmarine(old_pos_sub, command)
    square = battlefield[new_pos_sub[0]][new_pos_sub[1]] 
    if square == "*":
        hit_by_mine += 1
        if hit_by_mine < 3:
            battlefield[new_pos_sub[0]][new_pos_sub[1]] = "S"
            battlefield[old_pos_sub[0]][old_pos_sub[1]] = "-"
        else:
            battlefield[new_pos_sub[0]][new_pos_sub[1]] = "S"
            battlefield[old_pos_sub[0]][old_pos_sub[1]] = "-"
            x = new_pos_sub[0]
            y = new_pos_sub[1]
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{x}, {y}]!")
            game_on = False
    elif square == "-":
        battlefield[new_pos_sub[0]][new_pos_sub[1]] = "S"
        battlefield[old_pos_sub[0]][old_pos_sub[1]] = "-"
    elif square == "C":
        destroyed += 1
        if destroyed < 3:
            battlefield[new_pos_sub[0]][new_pos_sub[1]] = "S"
            battlefield[old_pos_sub[0]][old_pos_sub[1]] = "-"
        else:
            battlefield[new_pos_sub[0]][new_pos_sub[1]] = "S"
            battlefield[old_pos_sub[0]][old_pos_sub[1]] = "-"
            if destroyed == 3: 
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                game_on = False
    return battlefield, game_on, hit_by_mine, destroyed
 

def printBattlefield(battlefield):
    drawn = ""
    for row in battlefield:
        for square in row:
            drawn += square
        drawn += "\n"    
    drawn.strip()
    return drawn
    

game_on = True

for i in range(n):
    row = list(input())
    battlefield.append(row)

while game_on:
    pos_sub = locateSubmarine(battlefield)
    command = input()
    if game_on and command:
        battlefield, game_on, hit_by_mine, destroyed = updateBattlefield(pos_sub, command, game_on, hit_by_mine, destroyed)
    else:
        break


output = printBattlefield(battlefield)
print(output)

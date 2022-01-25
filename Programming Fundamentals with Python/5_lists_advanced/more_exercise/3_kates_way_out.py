# 3. Kate's Way Out
# Kate is stuck in a maze. You should help her to find her way out.
# On the first line, you will be given how many rows there are in the maze. On the following n
# lines, you will be given the maze itself. Here is a legend for the maze:
#     • "#" - means a wall; Kate cannot go through there
#     • " " - means empty space; Kate can go through there
#     • "k" - the initial position of Kate; start looking for a way out from there
# There are two options: Kate either gets out or not:
#     • If Kate can get out, print the following:
# "Kate got out in {number_of_moves} moves".
# Note: If there are two or more ways out, she always chooses the longest one.
#     • Otherwise, print: "Kate cannot get out".
n_lines = int(input())
#
counter = 0
# Positional variables:
k_pos = 0
path_pos = 0
# Finding the path for Kate:
maze_list = []
full_path = []
# Boolean vars:
kate_met = False
kate_out = False

kate_up = False
kate_down = False
blocked_up = False
blocked_down = False
number_of_moves = 0

def move():
    if ' ' not in maze_rows:
        if counter == n_lines:
            blocked_down = True
        elif counter <= n_lines // 2:
            blocked_up = True
            blocked = True
        else:
            blocked = False
    return blocked

for line in range(0, n_lines):
# # - means wall
    maze_rows = int(input())
    maze_list.append(maze_rows)

    counter += 1
for maze in maze_list:
    if move:
        print(f"Kate cannot get out")
    else:
        k_pos = maze.index('k')
        path_pos = maze.index(' ')
        full_path.append(path_pos)


if kate_out:
    print(f"Kate got out in {number_of_moves} moves")
# " " - means empty space
# k  - kate
#TODO:
# Build the rest of the maze...


print(f"Kate got out in {number_of_moves} moves")
print(f"Kate cannot get out")
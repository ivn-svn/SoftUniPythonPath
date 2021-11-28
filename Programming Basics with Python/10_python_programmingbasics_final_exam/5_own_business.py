# INPUT:
width = int(input())
length = int(input())
height = int(input())
# AUFGABE:
space_volume = width * length * height
space_f = space_volume
is_done_moving = False
while space_f > 0:
    cmd = input()
    if cmd == "Done":
        is_done_moving = True
        break
        # counters here: \/
    computers_count = int(cmd)
    space_f -= computers_count
if is_done_moving:
    print(f"{space_f} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(space_f)} Cubic meters more.")
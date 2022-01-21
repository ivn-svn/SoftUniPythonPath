lines = int(input())
tankcapacity = 255
addvol = 0
liters_water = 0
overflow = False
overflowvol = 0
for x in range(1, lines + 1):
    addvol = int(input())
    liters_water += addvol
    if liters_water > tankcapacity:
        overflow = True
        liters_water -= addvol
        print("Insufficient capacity!")
        continue
print(f"{liters_water}")
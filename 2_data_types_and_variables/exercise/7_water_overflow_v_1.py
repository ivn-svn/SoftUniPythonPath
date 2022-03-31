capacity = 255

tank = 0
n = int(input())
for i in range(n):
    water = int(input())

    if tank + water > capacity:
        print("Insufficient capacity!")
    else:
        tank += water
print(tank)
change = int(float(input()) * 100)
coins = 0
while change > 0:
    if change - 200 >= 0:
        change -= 200
    elif change - 100 >= 0:
        change -= 100
    elif change - 50 >= 0:
        change -= 50
    elif change - 20 >= 0:
        change -= 20
    elif change - 10 >= 0:
        change -= 10
    elif change - 5 >= 0:
        change -= 5
    elif change - 2 >= 0:
        change -= 2
    elif change - 1 >= 0:
        change -= 1
    coins += 1
print(coins)
init_energy = 100
init_coins = 100
enough = True
closed = False


def event_order(splt, init_e, init_c, en, cl):
    if splt[0] == 'rest':
        energy = int(splt[1])
        if init_e + energy <= 100:
            init_e += energy
            print(f"You gained {energy} energy.")
            print(f"Current energy: {init_e}.")
        elif init_e + energy >= 100:
            energy = 0
            print(f"You gained {energy} energy.")
            print(f"Current energy: {init_e}.")
    elif splt[0] == 'order':
        coins = int(splt[1])
        if init_e - 30 >= 0:
            init_e -= 30
            init_c += coins
            print(f"You earned {coins} coins.")
        else:
            init_e += 50
            print("You had to rest!")
    else:
        ingredient = splt[0]
        coins = int(splt[1])
        if init_c - coins >= 0:
            init_c -= coins
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            en = False
            cl = True
            return init_e, init_c, en, cl
    return init_e, init_c, en, cl



work_day_events = str(input()).split('|')

for item in work_day_events:
    splited = item.split('-')
    if closed == False:
        init_energy, init_coins, enough, closed = event_order(splited, init_energy, init_coins, enough, closed)

if enough:
    print(f"Day completed!\nCoins: {init_coins}\nEnergy: {init_energy}")

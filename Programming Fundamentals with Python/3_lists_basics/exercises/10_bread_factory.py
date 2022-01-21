# You have initial energy 100 and initial coins 100.
# You will be given a string, representing the working day events.
# Each event is separated with '|' (vertical bar): "event1|event2|event3…"
# Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}")
energy = 100
coins = 100
earned_coins = 0
#current_energy = 0
gained_energy = 0
#
ingredient = ''
#
event = input()
working_day_events = event.split('|')
for x in working_day_events:
    event1 = x.split('-')  # Split of the split of event, to hold the values separated by - (dash).
    # in any other case variables:
    if event1[0] == 'rest':
        gained_energy += int(float(event1[1]))
        #current_energy = energy
        energy += gained_energy
        if energy >= 100:
            energy -= int(float(event1[1]))
            gained_energy -= int(float(event1[1]))
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
    elif event1[0] == 'order':
        earned_coins = int(float(event1[1]))
        coins += earned_coins
        energy -= 30
        if energy > 0:
            print(f"You earned {earned_coins} coins.")
        if energy <= 0:
            energy += 50
            print("You had to rest!")
    else:
        ingredient = event1[0]
        coins -= int(float(event1[1]))
        if coins > 0:
            print(f"You bought {ingredient}.")
        elif coins <= 0:
            print(f"Closed! Cannot afford {ingredient}.")  # you went bankrupt
            break
            #
print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
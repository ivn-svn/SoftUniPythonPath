import math
party_size = int(input())  # You will receive a group size.
days = int(input()) # After that, you receive the days of the adventure.
coins = 0 #
food = 2
motivationalparty = False # WHETHER ITS MOTIVATIONAL PARTY TIME
for day in range(1, days + 1):
    if day % 10 == 0: # Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but every
        # 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
        party_size -= 2
    if day % 15 == 0: # every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
        party_size += 5
    coins += 50 - (food * party_size) # Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
    #
    if day % 3 == 0:
        coins -= (party_size * 3) # Every 3rd (third) day, you organize a motivational party, spending 3 coins per
        # companion for drinking water.
        motivationalparty = True
    else:
        motivationalparty = False
    if day % 5 == 0: # Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion. But if you have
        # a motivational party the same day, you spend additional 2 coins per companion.
        coins += (party_size * 20)
        if motivationalparty:
            coins -= (party_size * food)
coins_received = coins // party_size
print(f"{party_size} companions received {round(coins_received)} coins each.")

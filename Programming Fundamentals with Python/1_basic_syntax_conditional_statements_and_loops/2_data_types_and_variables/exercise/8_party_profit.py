# You will receive a party size. After that you receive the days of the adventure.
# Every day, you are earning 50 coins, but you also spent 2 coin per companion for food.

# Every 3rd (third) day, you have a motivational party, spending 3 coins per companion for drinking water.
# Every 5th (fifth) day you slay a boss monster and you gain 20 coins per companion. But if you have
# a motivational party the same day, you spent additional 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but every 15th (fifteenth) day
# 5 (five) new companions are joined at the beginning of the day.
# You have to calculate how much coins gets each companion at the end of the adventure.
party_size = int(input())
days_adventure = int(input())
#
#
water_cost = 0
food_cost = 0
boss_bonus = 0
additional_coin_cost = 0
#
coins = 0
total_cost = 0
#
motivational_party = False
for day in range(1, days_adventure + 1):
    coins += 50
    food_cost += party_size * 2
    if day % 3 == 0:
        motivational_party = True
        water_cost += party_size * 3
    if day % 5 == 0:
        boss_bonus += 20 * party_size
        if motivational_party:
            additional_coin_cost += 2 * party_size
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
total_cost = ((coins + boss_bonus) - (water_cost + food_cost + additional_coin_cost)) // party_size
print(total_cost)


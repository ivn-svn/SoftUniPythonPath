# Prices:
christmas_spirit = 0
#
ornament_price = 2
skirt_price = 5
garlands_price = 3
lights_price = 15
#
qty = int(input())
days = int(input())
#
budget = 0
for day in range(1, days + 1):
    # Да се обърне внимание, че при тази задача е от изключително значение реда на действията:
    # На 11-тия ден трябва да се извърши операцията с увеличаване на quantity, която впоследствие води и до разлика в
    # Total cost:
    # e.g. 60%
    # Input:
    # 4
    # 25
    # Outputs:
    # Total
    # cost: 946
    # Total
    # spirit: 239
    ####
    # 100% returns cost of 950, all the rest is the same.

    if day % 2 == 0:
        budget += (1 * qty) * ornament_price
        christmas_spirit += 5
    if day % 3 == 0:
        budget += (1 * qty) * skirt_price
        budget += (1 * qty) * garlands_price
        christmas_spirit += 13
        if day % 15 == 0:
            christmas_spirit += 30
    if day % 5 == 0:
        budget += (1 * qty) * lights_price
        christmas_spirit += 17
    if day % 10 == 0:
        christmas_spirit -= 20
        budget += 1 * skirt_price
        budget += 1 * garlands_price
        budget += 1 * lights_price
        if day == days:
            christmas_spirit -= 30
    if day % 11 == 0:
        qty += 2

print(f"Total cost: {budget}\nTotal spirit: {christmas_spirit}")
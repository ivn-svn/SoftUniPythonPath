quantity = int(input())
days = int(input())

ornament_price = 2
skirt_price = 5
garlands_price = 3
lights_price = 15

christmas_spirit = 0
budget = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 10 == 0:
        christmas_spirit -= 20
        budget += skirt_price + garlands_price + lights_price
        if day == days:
            christmas_spirit -= 30
    if day % 5 == 0:
        christmas_spirit += 17
        budget += lights_price * quantity
    if day % 15 == 0:
        christmas_spirit += 30
    if day % 3 == 0:
        christmas_spirit += 13
        budget += (garlands_price + skirt_price) * quantity
    if day % 2 == 0:
        christmas_spirit += 5
        budget += ornament_price * quantity
print(f"Total cost: {budget}\nTotal spirit: {christmas_spirit}")

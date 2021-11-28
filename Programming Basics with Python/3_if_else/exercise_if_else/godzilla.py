budget = float(input())
actors = int(input())
costume_price = float(input())
decor = budget * 0.1
costume_price_all = actors * costume_price
if actors >= 150:
  costume_price_all = costume_price_all - (costume_price_all * 0.1)
needed = decor + costume_price_all
left = budget - needed
left1 = abs(left)
if needed > budget:
    print(f'Not enough money!\nWingard needs {left1:.2f} leva more.')
elif needed <= budget:
    print(f'Action!\nWingard starts filming with {left1:.2f} leva left.')
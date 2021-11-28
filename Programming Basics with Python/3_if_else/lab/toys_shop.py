# prices counter variables
trip_price = float(input())
#
puzzle_price = float(2.60)
dolls_price = int(3)
teddies_price = float(4.10)
minion_price = float(8.20)
trucks_price = int(2)
# counter variables
puzzle_count = int(input())
dolls_count = int(input())
teddies_count = int(input())
minions_count = int(input())
trucks_count = int(input())
# --------------------------------------> sum of all toys: \/
toys_count = puzzle_count + dolls_count + teddies_count + minions_count + trucks_count
#  --------------------------------------> calculating the  total price of toys: \/
total_price_toys = (puzzle_count * puzzle_price) + (dolls_count * dolls_price) + (teddies_count * teddies_price) + \
                   (minions_count * minion_price) + (trucks_count * trucks_price)
price_reduction = total_price_toys * 0.25
after_reduction = total_price_toys - price_reduction
# --------------------------------------> IF STATEMENT
if toys_count >= 50: #  --------------------------------------> reduced price calculation: \/
    rent = after_reduction * 0.1
    money_after_rent = after_reduction - rent
    if money_after_rent >= trip_price:
        leva_left = money_after_rent - trip_price
        print(f"Yes! {leva_left:.2f} lv left.")
    else:
        not_enough = trip_price - money_after_rent
        print(f"Not enough money! {not_enough:.2f} lv needed.")
else:
    rent = total_price_toys * 0.1
    money_after_rent = total_price_toys - rent
    if money_after_rent >= trip_price:
        leva_left = money_after_rent - trip_price
        print(f"Yes! {leva_left:.2f} lv left.")
    else:
        not_enough = trip_price - money_after_rent
        print(f"Not enough money! {not_enough:.2f} lv needed.")

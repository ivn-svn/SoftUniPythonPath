movie_budget = float(input())
actors = int(input())
clothing_expense = float(input())
#
deco = movie_budget * 0.1
#
if actors >= 150:
    clothing_expense_all = clothing_expense * actors
    clothing_expense_all *= 0.9
    money_needed = deco + clothing_expense_all
    money_left = abs(money_needed - movie_budget)
#
if movie_budget < money_needed:
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")
elif movie_budget >= money_needed:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
#

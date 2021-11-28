film_budget = float(input())
extras_count = int(input())
single_clothing_price = float(input())

decor_price = film_budget * 0.1
t_cl_price = extras_count * single_clothing_price
if extras_count > 150:
    t_cl_price = t_cl_price * 0.9
total_expenses = decor_price + t_cl_price
if total_expenses <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {(film_budget - total_expenses):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {(total_expenses - film_budget):.2f} leva more.")
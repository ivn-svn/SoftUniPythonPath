# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ
# помогнете да разбере дали ще успее да събере необходимата сума.
# Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
money_needed = float(input())
money_available = float(input())
money_spent = 0
days_passed = 0
#
while money_available < money_needed and days_passed < 5:
    command = str(input())
    money = float(input())
    days_passed += 1
    if command == "save":
        money_available += money
        money_spent = 0
    elif command == "spend":
        money_available -= money
        money_spent += 1
        if money_available < 0:
            money_available = 0
#
if money_spent == 5:
    print("You can't save the money.")
    print(days_passed)
if money_available >= money_needed:
    print(f"You saved the money for {days_passed} days.")

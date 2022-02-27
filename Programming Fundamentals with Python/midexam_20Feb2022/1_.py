# Example inputs:
# 50
# 2
# 1.0 f
# 0.10 eggs
# 10.0 apr
# "Items purchased for {the cost of the items}$."
# "{neededMoney}$ more needed."
import math
# Input variables:
budget = float(input())
num_students = int(input())
#
flour_p = float(input())
eggs_p = float(input())
apron_p = float(input())
added_ap = num_students + math.ceil(num_students * 0.20)
# Standard price per individual item:
free_packages = 0 # 
for i in range(0, num_students):
    if i % 5 == 0:
        free_packages += 1
# Price of avail_set
total_price = apron_p * added_ap + ((eggs_p * 10) * num_students) + flour_p * (num_students - free_packages)
#
item_costs = 0
money_needed = 0
# EVery fifth package of flour is free:

if total_price > budget:
    money_needed = total_price - budget
    print(f"{money_needed:.2f}$ more needed.")

elif total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
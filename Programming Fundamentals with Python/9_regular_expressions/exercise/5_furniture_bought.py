# Write a program that calculates the total cost of bought furniture. You will be given information about each purchase
# on separate lines until you receive the command "Purchase". Valid information should be in the format:
# ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number.
# You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"
import re

command = ""
pattern = r">>(\w+)<<(\w+|\w+.\w+)!(\w+)"

stuff_list = []
# Stuff list digestion:
total_price = 0
quantity = 0
furniture_bought = []
item_price = 0
print_items = ""
end_cycle = False

while command.lower() != "purchase" and not end_cycle:
    command = input()
    if command.lower() == "purchase":
        end_cycle = True
        break
    else:
        appendable = re.findall(pattern, command)
        stuff_list += appendable

for item in stuff_list:
    furniture_bought.append(item[0])
    item_price = float(item[1])
    quantity = int(item[2])
    total_price += item_price * quantity


print(f'Bought furniture:')
for furniture in furniture_bought:
    print(furniture)
print(f"Total money spend: {total_price}")

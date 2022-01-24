
# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you decide 
# to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type                  Price:
# Clothes               50.00
# Shoes                 35.00
# Accessories           20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce
#  the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if the budget
# after selling all the items is enough for buying the train ticket.


# Key Variables
items_input = input().split('|')
initial_budget = int(input())
budget = initial_budget
#
ticket = 150 
items = []
markup = 0.40
profit = 0
list_new_prices = []
# {type->price|type->price|type->price……|type->price}{budget}
#
item_type = ''
price_list = [50.00, 35.00, 20.50]


def item_price_check(clot, itt, itp):
    if itt == "clothes":
        max_price = clot[0]
    if itt == "shoes":
        max_price = clot[1]
    elif itt == "accessories":
        max_price = clot[2]
        
    if itp > max_price:
        return True
    else:
        return False
    
    
for item in items_input:
    items = item.split('->')
    item_type = items[0].lower()
    item_price = float(items[1])

    canbuy = item_price_check(price_list, item_type, item_price)

    if canbuy == False and budget - item_price > 0:
        budget -= item_price
        profit += item_price * markup
        item_price += item_price * markup
        list_new_prices.append(f"{item_price:.2f}")

if initial_budget + profit >= ticket:
    for new in list_new_prices:
        print(f"{new}", end=" ")
    print(f"\nProfit: {profit:.2f}")
    print("Hello, France!")

else:
    for new in list_new_prices:
        print(f"{new}", end=" ")
    print(f"\nProfit: {profit:.2f}")
    print("Not enough money.")
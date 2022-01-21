# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
#     • If the product doesn't exist yet, add it with its starting quantity.
#     • If you receive a product, which already exists, increases its quantity by the input quantity
# and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", ' \
#                          'keep adding items. Finally, ' \
#                          'print all items with their names and the total price of each product.
# Input
#     • Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
#     • The product data is always delimited by a single space.
# Output
#     • Print information about each product in the following format:
# "{product_name} -> {total_price}"
#     • Format the total price to the 2nd digit after the decimal separator.
# Input
# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy
# _____________________________
# Output
# Beer -> 220.00
# IceTea -> 75.00
# NukaCola -> 264.00
# Water -> 500.00
price_dict = {}
quantity_dict = {}
user_input = ''
totalprice_dict = {}
while user_input != 'buy':
    user_input = input()
    if user_input == 'buy':
        break
    else:
        user_input = user_input.split(' ')
        name = user_input[0]
        price = float(user_input[1])
        quantity = int(user_input[2])
        if name not in price_dict.keys() and name not in quantity_dict.keys():
            quantity_dict[name] = quantity
            price_dict[name] = price
        elif name in price_dict.keys() and name in quantity_dict.keys():
            quantity_dict[name] += quantity
            price_dict[name] = price 
totalprice_dict = {}

for (keys, values) in price_dict.items():
    totalprice_dict[keys] = values * quantity_dict[keys]
for (keys, values) in totalprice_dict.items():
    print(f"{keys} -> {values:.2f}")  
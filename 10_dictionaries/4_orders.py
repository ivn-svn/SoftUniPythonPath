# Write a program that keeps information about products and their prices.
# Each product has a name, a price and a quantity.
# If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists, increase its quantity by the input quantity and if
# its price is different, replace the price as well.
# You will receive products' names, prices and quantities on new lines. Until you receive the command ' \
#                          '"buy", keep adding items. When you do receive the command "buy", ' \
#                          'print the items with their names and total price of all the products with that name.
data_input = input().split(" ")
#
dict_products = {
    "name": 0,
    "price": 0,
    "quantity": 0
}
command = ''
while command != 'buy':
    if data_input
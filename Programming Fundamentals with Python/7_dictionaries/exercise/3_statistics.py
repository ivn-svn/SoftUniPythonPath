#  You will be receiving key-value pairs on separate lines separated
# by ": " until you receive the command "statistics"
#  Sometimes you may receive a product more than once. In that case add
# up the quantities
#  When you receive the "statistics" command, print the output as in
# the example

products = {}
command = input()
total = 0
quantityall = 0

while command != "statistics":
    product = command.split(": ")[0]
    quantity = command.split(": ")[1]
    # split the command and get the product and the quantity
    if product not in products:
        products[product] = 0
    products[product] += int(quantity)
    command = input()
print("Products in stock:")
for i in products:
    print(f"- {i}: {products[i]}")
    total += 1
    quantityall += int(products[i])

print(f"Total Products: {total}\n"
      f"Total Quantity: {quantityall}")
#
# Products in stock:
# - bread: 5
# - cheese: 2
# - ham: 1
# Total Products: 3
# Total Quantity: 8

# Write a function that calculates the total price of an order and prints it on the console. The function should receive
# one of the following products: coffee, coke, water, snacks; and a quantity of the product.
# The prices for a single piece of each product are:
#
# • coffee - 1.50
# • water - 1.00
# • coke - 1.40
# • snacks - 2.00
inputedstr = input()
quantity = int(input())
coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00
#
total_price = 0
#
def total_calc(a, b):
    if inputedstr == 'coffee':
        a = coffee
    elif inputedstr == 'water':
        a = water
    elif inputedstr == 'coke':
        a = coke
    elif inputedstr == 'snacks':
        a = snacks
    total_price = a * b
    return f"{total_price:.2f}"
print(total_calc(inputedstr, quantity))
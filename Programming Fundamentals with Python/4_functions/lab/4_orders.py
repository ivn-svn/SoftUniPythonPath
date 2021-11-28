# Write a function that calculates the total price of an order and prints it on the console.
# The function should receive one of the following products: coffee, coke, water, snacks; and a quantity of the product.
# The prices for a single piece of each product are:
# coffee - 1.50
# water - 1.00
# coke - 1.40
# snacks - 2.00
product = str(input())
quantity = int(input())
#
#
def order_price(q, p):
    if product == "coffee":
        p = 1.50
    elif product == "coke":
        p = 1.40
    elif product == "water":
        p = 1.00
    elif product == "snacks":
        p = 2.00
    price_of_order = q * p
    return price_of_order
print(f'{order_price(quantity, product):.2f}')

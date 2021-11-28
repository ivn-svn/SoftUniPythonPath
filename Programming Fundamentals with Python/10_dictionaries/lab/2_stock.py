# If you have the product, print "We have {quantity} of {product} left"
# Otherwise, print "Sorry, we don't have {product}"
values = input().split(" ")
searched_products = input().split(" ")
bakery = {}
n = len(values)
for i in range(0, n, 2):
    # 0, 2, 4, 6, 8...
    food = values[i]
    quantity = int(values[i + 1])
    bakery[food] = quantity #e.g.: key[] = value | This is a Python single value assignment into an object,
    # either a dictionary or a list. The Python subscript operator a[b] works on both a dictionary and a list.
    # | Signle value assignment: https://qr.ae/pNivpM
for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
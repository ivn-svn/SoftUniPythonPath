# https://softuni.bg/downloads/svn/soft-tech/May-2020/Python/07-Dictionaries/07.%20Dictionaries-Lab.docx
# This is your first task in your new job. You were tasked to create a list of the stock in a bakery and you really
# don't want to fail at you first day at work.
# You will receive a single line containing some food (keys) and quantities '
# '(values). They will be separated by a single space (the first element is the key, the second – the value and so on).'
# ' Create a dictionary with all the keys and values and print it on the console
# elements = input().split(" ")
# bakery = {} # bakery = dict()
# for i in range(0, len(elements), 2):
#     key = elements[i]
#     value = elements[i + 1]
#     bakery[key] = int(value)
# print(bakery)
# #
# products = {}
# #
# data = input()
# elements = data.split(" ")
# for index in range(0, len(elements), 2):
#     product_name = elements[index]
#     product_quantity = elements[index + 1]
#     products[product_name] = int(product_quantity)
# #
# print(products)

#
# bakery_str = input()
#

def solve(bakery_str):
    values = bakery_str.split(" ")
    bakery = {}
    n = len(values)
    for i in range(0, n, 2):
        # 0, 2, 4, 6, 8...
        food = values[i]
        quantity = int(values[i + 1])
        bakery[food] = quantity #e.g.: key[] = value | This is a Python single value assignment into an object,
        # either a dictionary or a list. The Python subscript operator a[b] works on both a dictionary and a list.
        # | Signle value assignment: https://qr.ae/pNivpM
    print(bakery)


solve(input())

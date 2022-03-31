# data_input = '' .lower()
# water = 'water'
# sand = 'sand'
# fish = 'fish'
# sun = 'sun'
# counter = 0
# y = 0
# z = 0
# x = 0
# j = 0
# while True:
#     try:
#         data_input = input().lower()
#     #for x in data_input:
#         if water in data_input:
#             z = data_input.count(water)
#         if fish in data_input:
#             x = data_input.count(fish)
#         if sun in data_input:
#             j = data_input.count(sun)
#         if sand in data_input:
#             y = data_input.count(sand)
#     except EOFError:
#         print(y + z + j + x)
data_input = '' .lower()
water = 'water'
sand = 'sand'
fish = 'fish'
sun = 'sun'
counter = 0
y = 0
z = 0
x = 0
j = 0
data_input = input().lower()
if water in data_input:
    z = data_input.count(water)
if fish in data_input:
    x = data_input.count(fish)
if sun in data_input:
    j = data_input.count(sun)
if sand in data_input:
    y = data_input.count(sand)
print(y + z + j + x)
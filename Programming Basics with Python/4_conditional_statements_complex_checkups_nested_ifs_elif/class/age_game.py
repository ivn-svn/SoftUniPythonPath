age = int(input())
budget = int(input())
item_price = int(input())
#
if age >= 14 and budget >= item_price:
    print('You can buy the game.')
elif age <= 14 and budget >= item_price:
    print('You are too young.')

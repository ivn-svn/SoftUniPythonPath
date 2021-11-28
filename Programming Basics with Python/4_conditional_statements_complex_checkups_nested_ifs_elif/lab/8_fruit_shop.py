# цена
# 2.50 banana
# 1.20 apple
# 0.85 orange
# 1.45 grapefruit
# 2.70 kiwi
# 5.50 pineapple
# 3.85 grapes
#
# цена
# 2.70 banana
# 1.25 apple
# 0.90 orange
# 1.60 grapefruit
# 3.00 kiwi
# 5.60 pineapple
# 4.20 grapes
fruit = input().lower()
weekday = input().lower()
amount = float(input())
#
fruit_price = 0
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
#
fruit_list = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
if weekday in week:
    if fruit == "banana":
        fruit_price = 2.50
    elif fruit == "apple":
        fruit_price = 1.20
    elif fruit == "orange":
        fruit_price = 0.85
    elif fruit == "grapefruit":
        fruit_price = 1.45
    elif fruit == "kiwi":
        fruit_price = 2.70
    elif fruit == "pineapple":
        fruit_price = 5.50
    elif fruit == "grapes":
        fruit_price = 3.85
    price = fruit_price * amount
    print(f"{price:.2f}")
elif weekday in weekend:
    if fruit == "banana":
        fruit_price = 2.70
    elif fruit == "apple":
        fruit_price = 1.25
    elif fruit == "orange":
        fruit_price = 0.90
    elif fruit == "grapefruit":
        fruit_price = 1.60
    elif fruit == "kiwi":
        fruit_price = 3.00
    elif fruit == "pineapple":
        fruit_price = 5.60
    elif fruit == "grapes":
        fruit_price = 4.20
    price = fruit_price * amount
    print(f"{price:.2f}")
else:
    print("error")



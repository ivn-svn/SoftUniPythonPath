flowers_type = input()
flowers_count = int(input())
budget = int(input())
#
total_price = 0
#
if flowers_type == "Roses":
    total_price * flowers_count * 5
    if flowers_count > 80:
        total_price * flowers_count * 0.9

elif flowers_type == "Dahlias"
    pass
elif flowers_type == "Tulips"
    pass
elif flowers_type == "Narcissus"
    pass
    if flowers_count < 120:
        total_price = flowers_count * 3
elif flowers_type == "Gladiolus"
    total_price = flowers_count * 2.50
    if flowers_count < 80:
        total_price *= 1.2
if budget >= total_price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {нужната сума} leva more.")
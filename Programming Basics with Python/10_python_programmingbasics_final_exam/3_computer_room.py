#__________________________________
# Март до Май     | Юни до Август |
# Ден | 10.50лв/ч | 12.60лв/ч     |
# Нощ | 8.4лв/ч   | 10.20лв/ч     |
#__________________________________
# Предлагат се и следните отстъпки в следната последователност:
#     • За група от четирима или повече човека, цената на човек се намалява с 10%
#     • При 5 или повече часа прекарани, цената се намалява с 50% на човек
#
# Да се напише програма, която изчислява цената на човек за час и общата сума.
#
# Входът се чете от конзолата и съдържа точно 4 реда:
#     • На първия ред - месецът - текст с възможности "march", "april", "may", "june", "july", "august"
#     • На втория ред - броят на прекараните часове, цяло число [1...10]
#     • На третия ред - броят на хората в групата, цяло число [1...10]
#     • На четвъртия ред - времето от деня – текст с възможности: "day","night"
# Изход
# Да се отпечатат на конзолата два реда:
#     • На първия ред: "Price per person for one hour: {цена на човек на час}"
#     • На втория ред: "Total cost of the visit: {общата сума}"
# Цената да бъде закръглена до втория знак след десетичната запетая.
#

# Variables:
price_hour_per_person = 0
total_sum = 0
# DISCOUNT VARIABL:
discount = 0
# USER INPUT
month = str(input())
hours_spent = int(input())
participants_num = int(input())
day_time = str(input())
# checkups
# spring
if month == "march":
    if day_time == "day":
        price_hour_per_person = 10.5
    elif day_time == "night":
        price_hour_per_person = 8.4
elif month == "april":
    if day_time == "day":
        price_hour_per_person = 10.5
    elif day_time == "night":
        price_hour_per_person = 8.4
elif month == "may":
    if day_time == "day":
        price_hour_per_person = 10.5
    elif day_time == "night":
        price_hour_per_person = 8.4
# Summer time:
elif month == "june":
    if day_time == "day":
        price_hour_per_person = 12.6
    elif day_time == "night":
        price_hour_per_person = 10.2
elif month == "july":
    if day_time == "day":
        price_hour_per_person = 12.6
    elif day_time == "night":
        price_hour_per_person = 10.2
elif month == "august":
    if day_time == "day":
        price_hour_per_person = 12.6
    elif day_time == "night":
        price_hour_per_person = 10.2
#
discounter = False
if participants_num >= 4 or hours_spent >= 5:
    discounter = True
    if participants_num >= 4:
        price_hour_per_person *= 0.9
    else:
        pass
    if hours_spent >= 5:
        price_hour_per_person *= 0.5
    else:
        pass
# price_hour_per_person *= discount
# discounted = price_hour_per_person * discount
# discount_sum = price_hour_per_person * hours_spent
total_sum = price_hour_per_person * hours_spent * participants_num
# OUTPUT
print(f"Price per person for one hour: {price_hour_per_person:.2f}")
print(f"Total cost of the visit: {total_sum:.2f}")

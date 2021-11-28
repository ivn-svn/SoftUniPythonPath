room_one_person = 18 # x
apartment = 25.00 # x
president_apartment = 35 # x
acco = 0
# User input for the length of the stay in days:
stay = int(input()) # x
room_type = str(input()) # x
review = str(input()) # x
# The nights a person stays in the hotel.
nights = stay - 1 # x
# Discount:
price_of_stay = acco * nights
if room_type == "apartment":
    if stay < 10:
        price_of_stay = apartment * nights * 0.7
elif room_type == "president apartment":
    if stay < 10:
        price_of_stay = apartment * nights * 0.9
elif room_type == "apartment":
    if stay > 9 and stay < 16:
        price_of_stay = apartment * nights * 0.65
elif room_type == "president apartment":
    if stay > 9 and stay < 16:
        price_of_stay = apartment * nights * 0.85
elif room_type == "apartment":
    if stay > 15:
        price_of_stay = apartment * nights * 0.5
elif room_type == "president apartment":
    if stay > 15:
        price_of_stay = apartment * nights * 0.8
# Calculating the price of stay:
# Discounts table per type of apartment:
# |-----------------------------------------------------|
# | room    | discount < 10 d | 10 - 15 days | 15+ days |
# | one per | no discount     | no discount  | no disc  |
# | apart   |  30%       x    | 35%     x    | 50%  x   |
# | presapt |  10%       x    | 15%     x    | 20%  x   |
# |-----------------------------------------------------|
# Code to calculate the price after the discount:
# After calculation, check if review is positive or negative:
if review == "positive":
    price_of_stay = price_of_stay * 0.25 + price_of_stay
elif review == "negative":
    price_of_stay = 0.9 * price_of_stay
print(f"{price_of_stay:.2f}")
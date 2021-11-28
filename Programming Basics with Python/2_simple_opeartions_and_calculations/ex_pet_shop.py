import math
dogs_count = int(input())
other_animals_count = int(input())
#
dogs_food_price = dogs_count * 2.5
other_animals_food_price = other_animals_count * 4
total_cost = dogs_food_price + other_animals_food_price
print(f'{total_cost:.2f} lv.')
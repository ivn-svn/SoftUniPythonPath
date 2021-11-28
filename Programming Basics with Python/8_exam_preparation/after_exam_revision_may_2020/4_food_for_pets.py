import math
#
days_num = int(input())
total_amount_food = float(input())
#
percent_food_eaten_by_dog = 0
percent_food_eaten_by_cat = 0
#
all_food_eaten = 0
#
third_day_bonus_cookie = 0
dog_food = 0
cat_food = 0
dog_food_eaten = 0
cat_food_eaten = 0
for day in range(1, days_num + 1):
    #
    dog_food = int(input())
    cat_food = int(input())
    food_4_the_day = dog_food + cat_food
    if day % 3 == 0:
        third_day_bonus_cookie += 0.1 * food_4_the_day
    all_food_eaten += food_4_the_day
    dog_food_eaten += dog_food
    cat_food_eaten += cat_food
    #
# Statement has no effect link to explanation:
# https://help.semmle.com/wiki/display/PYTHON/Statement+has+no+effect
# Output Variables Definition
cookies_eaten = math.ceil(third_day_bonus_cookie)
percent_food_eaten = (all_food_eaten / total_amount_food) * 100
percent_food_eaten_by_dog = (dog_food_eaten / all_food_eaten) * 100
percent_food_eaten_by_cat = (cat_food_eaten / all_food_eaten) * 100
# OUTPUT \/
print(f"Total eaten biscuits: {cookies_eaten}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_food_eaten_by_dog:.2f}% eaten from the dog.")
print(f"{percent_food_eaten_by_cat:.2f}% eaten from the cat.")



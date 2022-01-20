people_n = int(input())
capacity_p = int(input())
calc_courses = people_n // capacity_p
people_left = people_n % capacity_p
if capacity_p >= people_n or people_left > 0:
    additional_courses = capacity_p // people_left
    calc_courses += additional_courses
    print(calc_courses)
elif people_left == 0:
    print(calc_courses)
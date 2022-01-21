# Kids drink toddy, Teens drink coke, Young adults drink beer, Adults drink whisky.
# # Make a program that receives an age, and returns what they drink.
# # Rules:
# # Kids under 14 years old.
# # Teens under 18 years old.
# # Young adults under 21 years old.
# # Adults above 21.
# # Note: All the values except the last one are inclusive!
# age_range = int(input())
# if age_range >= 14 and age_range < 18:
#     print("drink coke")
# elif age_range >= 18 and age_range <= 21:
#     print("drink beer")
# elif age_range > 21:
#     print("drink whisky")
# else:
#     print("drink toddy")
age_range = int(input())
if age_range <= 14:
    print("drink toddy")
elif age_range <= 18:
    print("drink coke")
elif age_range <= 21:
    print("drink beer")
elif age_range > 21:
    print("drink whisky")
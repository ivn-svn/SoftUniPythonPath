# Calculate how many courses will be needed to elevate n persons by using an elevator of capacity of p persons.
# The input holds two lines: the number of people n and the capacity p of the elevator.
import math
people_n = int(input())
capacity_p = int(input())
calc_courses = people_n // capacity_p
people_left = people_n % capacity_p
if capacity_p >= people_n:
    print("All the persons fit inside in the elevator.\n"
          "Only one course is needed.")
elif people_left != 0:
    people_per_course = (people_n - people_left) // calc_courses
    additional_courses = capacity_p // people_left
    print(f"{calc_courses} courses * {people_per_course} people + {additional_courses} course * {people_left} persons")
elif people_left == 0:
    people_per_course = (people_n - people_left) // calc_courses
    print(f"{calc_courses} courses * {people_per_course} people")
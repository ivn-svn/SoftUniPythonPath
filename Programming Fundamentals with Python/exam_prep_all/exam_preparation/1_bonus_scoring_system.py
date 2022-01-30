# https://judge.softuni.bg/Contests/Practice/Index/2028#0
import math
students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())
max_bonus_points = 0
bonus_attendances = 0
if students_count >= 0 and lectures_count >= 0:
    for x in range(students_count):
        student_attendances = int(input())
        total_bonus = student_attendances / lectures_count * (5 + additional_bonus)
#
        if total_bonus >= max_bonus_points:
            max_bonus_points = total_bonus
            stud_att_counted = student_attendances
        else:
            pass
print(f"\nMax Bonus: {math.ceil(max_bonus_points)}.\nThe student has attended {stud_att_counted} lectures.")
# example input:
# 5
# 25
# 30
# 12
# 19
# 24
# 16
# 20
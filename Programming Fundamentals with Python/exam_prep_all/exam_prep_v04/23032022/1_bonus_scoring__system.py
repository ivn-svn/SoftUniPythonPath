# https://judge.softuni.org/Contests/Practice/Index/2028#0
import math


def calculate_bonus(att_ct, cour_lect, add_bon):
    tot_bon = (att_ct / cour_lect) * (5 + add_bon)
    return tot_bon


num_studs = int(input())
num_lectures = int(input())
additional_bonus = int(input())

max_bonus_pts = 0
total_bonus_pts = 0
stud_attendance = 0

attendance_bonus_dict = {}
for student in range(0, num_studs):
    attendance_count = int(input())
    total_bonus_pts = calculate_bonus(attendance_count, num_lectures, additional_bonus)
    attendance_bonus_dict[attendance_count] = total_bonus_pts

max_bonus_key = max(zip(attendance_bonus_dict.values(), attendance_bonus_dict.keys()))[1]  # finding max values in dict
max_bonus_pts = max(zip(attendance_bonus_dict.values(), attendance_bonus_dict.keys()))[0]  # & referencing the value2key
stud_attendance = max_bonus_key

max_bonus_pts = math.ceil(max_bonus_pts)
stud_attendance = math.ceil(stud_attendance)
print(f"Max Bonus: {max_bonus_pts}.")
print(f"The student has attended {stud_attendance} lectures.")

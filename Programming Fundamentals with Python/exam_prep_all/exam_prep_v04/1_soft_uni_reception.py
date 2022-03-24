# https://judge.softuni.org/Contests/Practice/Index/2474#0
employee1_eff = int(input())
employee2_eff = int(input())
employee3_eff = int(input())

students_count = int(input())
stud_per_hour = (employee1_eff + employee2_eff + employee3_eff)
# print(stud_per_hour)

hour = 1
while students_count > 0:
    # print(hour)
    if hour % 4 != 0:
        if students_count - stud_per_hour <= 0:
            students_count -= stud_per_hour
            break
        else:
            students_count -= stud_per_hour
            hour += 1
    else:
        hour += 1
time = hour
print(f"Time needed: {time}h.")
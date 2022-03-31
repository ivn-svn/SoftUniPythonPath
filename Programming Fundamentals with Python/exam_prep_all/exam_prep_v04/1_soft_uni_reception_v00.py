# https://judge.softuni.org/Contests/Practice/Index/2474#0
time = 0

employee1_eff, employee2_eff, employee3_eff, students_count = int(input()), int(input()), int(input()), int(input())

stud_per_hour = (employee1_eff + employee2_eff + employee3_eff)

while students_count > 0:
    if students_count > 0:
        if time % 4 == 0:
            time += 1
        else:
            if students_count - stud_per_hour <= 0:
                students_count -= stud_per_hour
                break
            else:
                students_count -= stud_per_hour
                time += 1
    else:
        break
print(f"Time needed: {time}h.")

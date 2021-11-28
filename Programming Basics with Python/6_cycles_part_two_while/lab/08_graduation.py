student_name = str(input())
grades_passed = 1
sum_marks = 0
while grades_passed <= 12:
    current_mark = float(input())
    if current_mark >= 4:
        grades_passed += 1
        sum_marks += current_mark
average_mark = sum_marks / 12
print(f"{student_name} graduated. Average grade: {average_mark:.2f}")
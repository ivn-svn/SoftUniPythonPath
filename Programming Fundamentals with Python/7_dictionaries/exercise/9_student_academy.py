# # https://judge.softuni.org/Contests/1737
# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with
# an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.
average_grade = 0
name_grade_dict = {}
excellent_studs_name_grade_dict = {}
n = int(input())
for idx in range(0, n):

    name = input()
    grade = float(input())
    if name in name_grade_dict.keys():
        name_grade_dict[name].append(grade)
    else:
        name_grade_dict[name] = []
        name_grade_dict[name].append(grade)

for (k,v) in name_grade_dict.items():
    avg = sum(v) / len(v)
    if avg >= 4.50:
        excellent_studs_name_grade_dict[k] = avg

for (k,v) in excellent_studs_name_grade_dict.items():
    print(f"{k} -> {v:.2f}")

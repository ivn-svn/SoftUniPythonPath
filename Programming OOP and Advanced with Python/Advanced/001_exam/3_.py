def students_credits(*args):
    course_list = []
    sum_credits = 0
    for courses in args:
        course_name = courses.split("-")[0]
        credits = courses.split("-")[1]
        max_test_points = courses.split("-")[2]
        results = courses.split("-")[3]
        course_list.append([course_name, int(credits), int(max_test_points), int(results)])
        sum_credits += int(credits)
    if sum_credits >= 240:
        print(f"Diyan gets a diploma with {sum_credits} credits.")
    else:
        credits_needed = 240 - sum_credits
        print(f"Diyan needs {credits_needed} credits more for a diploma.")
    return course_list

'''

•	Diyan's achievement message:
o	If the sum of all of Diyan's credits is more than or equal to 240, return: "Diyan gets a diploma with {total credits} credits."
o	Otherwise, return: "Diyan needs {credits needed} credits more for a diploma."
•	Information for each course and Diyan's credits:
o	"{course name} - {diyan's credits}"
o	Note: Each course data should be on a new line.
•	All credits must be formatted to the first decimal place.

'''

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)


for c in course_list:
    print(f"{c[0][0]} - {c[1][1]}", end="\n")

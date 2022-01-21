#     8. Courses
# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users.
#     For each course, print the registered users.
# Input
#     • Until the "end" command is received, you will be receiving input lines in the format:
# "{course_name} : {student_name}"
#     • The product data is always delimited by " : "
# Output
#     • Print the information about each course in the following format:
# "{course_name}: {registered_students}"
#     • Print the information about each student in the following format:
# "-- {student_name}"
# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end
command_input = ''
endloop = False
students_courses_db = {}
while endloop != True:
    command_input = input()
    if command_input != 'end':
        command_input = command_input.split(' : ')
        course_name = command_input[0]
        student_name = command_input[1]
        if student_name not in students_courses_db.values() and course_name in students_courses_db.keys():
            students_courses_db[course_name] = students_courses_db[course_name] + [student_name]
        elif course_name not in students_courses_db.items():
            students_courses_db[course_name] = [student_name]
        objlen = len(students_courses_db[course_name])


    elif command_input == 'end':
        endloop = True
        break
for (keys, values) in students_courses_db.items():
    print(f'{keys}: {len(students_courses_db[keys])}')
    for value in values:
        print(f'-- {value}')

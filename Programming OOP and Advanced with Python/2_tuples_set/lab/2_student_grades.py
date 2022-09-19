#   7
#   Peter 5.20
#   Mark 5.50
#   Peter 3.20
#   Mark 2.50
#   Alex 2.00
#   Mark 3.46
#   Alex 3.00
#
# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and their grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.


def Average(lst):
    return sum(lst) / len(lst)
  

num_studs = int(input())


studs_dict = dict()

for i in range(0, num_studs):
    stud = input()
    student = stud.split(' ')[0]
    mark = round(float(stud.split(' ')[1]), 2)
    if student in studs_dict.keys():
        studs_dict[student].append(mark)
    else: 
        studs_dict[student] = [mark]

for students, marks in studs_dict.items():
    # Driver Code 4 Average function
    marks_float = [round(float(f), 2) for f in marks]
    lst = marks_float
    if lst:
        average = Average(lst)
    #
    marks = ["{:.2f}".format(z) for z in marks]
    marks_joined = ' '.join(marks)
    print(f"{students} -> {marks_joined} (avg: {average:.2f})")
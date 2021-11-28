# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.
n = int(input()) # number of people to go on the elevator
p = int(input()) # people capacity
second_course_ppl = n % p
num_courses = n // p
if second_course_ppl != 0:
    num_courses += 1
print(num_courses)

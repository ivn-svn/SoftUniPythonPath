# https://python-book.softuni.bg/chapter-02-simple-calculations-exam-problems.html
import math

l = float(input())   # room length
w = float(input())   # room width
if 3 <= w <= l <= 100:
    l *= 100
    w *= 100
    num_seats = 0
    rows = l // 120
    columns = (w - 100) // 70
    # workplace: 70 * 120
    # Entrance  - 1 workplace
    # katedra = - 2 workplaces
    #
    num_seats = rows * columns - 3
    #
    print(math.floor(num_seats))

# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.
year_input = input()

def yr_check(yr, bol):
    newyear = list(str(yr))
    for digit in newyear:
        if newyear.count(digit) > 1:
            bol = False
            yr += 1
        else:
            bol = True
    return yr, bol

happy_year = False
while happy_year != True:
    happy = yr_check(int(year_input), happy_year)
    happy_year = happy[1]
    year_input = happy[0]
    print(happy_year, year_input)
    if happy_year == True:
        break
else:
    print(happy_year, year_input)

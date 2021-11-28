# You're saying good-bye your best friend, "See you next happy year". ' \
# 'Happy Year is the year with only distinct digits, (e.g) 2018. Write a program that receives an integer number and ' \
#    'finds the next happy year.
# Input
# 8989
# Output
# 9012
year_input = int(input())
year_array = list(str(year_input))
is_happy_year = 0
distinct_check = False
not_distinct = False
repeat_counter = 0
digits_checked = 0
while distinct_check == False and not_distinct == False:


    for j in year_array:
        if repeat_counter == 1 and digits_checked == 4:
            is_happy_year = "".join(year_array)

            distinct_check = True

            print(f"See you next happy year {is_happy_year}")
            break
        elif digits_checked > 4 and repeat_counter > 1:
            print('********* no happy year')
            not_distinct = True
            break

        digits_checked += 1
        repeat_counter = year_array.count(j)


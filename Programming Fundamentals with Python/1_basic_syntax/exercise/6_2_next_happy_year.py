# You're saying good-bye your best friend, "See you next happy year". ' \
# 'Happy Year is the year with only distinct digits, (e.g) 2018. Write a program that receives an integer number and ' \
#    'finds the next happy year.
# Input
# 8989
# Output
# 9012
initial_year_input = int(input())
isunique = False
next_happy_year = 0
distinct_check = False
repeat_counter = 0
repeated = 0
digits_checked = 0
while distinct_check == False:
    for x in str(initial_year_input):
        lstyr = list(str(initial_year_input))
        repeat_counter = lstyr.count(x)
        if x in lstyr and repeat_counter > 1:
            print('not happy year')
            if digits_checked == 1 and repeat_counter > 1:
                initial_year_input += 1000
            elif digits_checked == 2 and lstyr[1] == x:
                initial_year_input += 100
            elif digits_checked == 3 and lstyr[2] == x:
                initial_year_input += 10
            elif digits_checked == 4 and lstyr[3] == x:
                initial_year_input += 1
        digits_checked += 1
        if digits_checked == 4 and repeat_counter == 1:
            distinct_check = True
        initial_year_input += 1
print(initial_year_input)
            # repeat_counter = lstyr.count(x)


    # for s in str(initial_year_input):
    # for j in str(next_happy_year):
    #     lstyr = list(str(next_happy_year))
    #     if j in lstyr:
    #         repeat_counter = lstyr.count(j)
    #     if repeat_counter > 1 and digits_checked == len(str(next_happy_year)):
    #         repeated += 1
    #         print('***no happy year***')
    #         continue
    #     elif repeat_counter == 1 and digits_checked == len(str(next_happy_year)) and repeated == 0:
    #         print(next_happy_year)
    #         distinct_check = True
    #         break
    #     digits_checked += 1

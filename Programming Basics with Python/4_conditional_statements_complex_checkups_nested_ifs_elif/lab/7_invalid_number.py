# number = int(input())
# #
# for number in range(100, 200) or number == 0:
#     print()
# else:
#     print("invalid")
number = int(input())
is_number_valid = number >= 100 and number <= 200 or number == 0
if not is_number_valid:
    print('invalid')

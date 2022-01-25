# Read through a string and skip through it, extract the hidden message.
# Example string: skipTest_String044170
#
# [0, 4, 7]
# [4, 1, 0]

user_input = list(input())
num_list = [int(x) for x in user_input if x.isdigit()]
str_list = [str(y) for y in user_input if y.isdigit() == False]
# In the take list, you should keep all digits at an even index.
# In the skip list, you should keep all digits at an odd index.
take_list = [num_list[digit] for digit in range(0, len(num_list)) if digit % 2 == 0]
skip_list = [num_list[digit] for digit in range(0, len(num_list)) if digit % 2 == 1]
lncount = 0
str_list = ''.join(str_list)

final_str = ''
for i in range(len(take_list)):
    if int(take_list[i]) > 0:
        start = lncount
        lncount += int(take_list[i])
        final_str += str_list[slice(start, lncount)]

    if int(skip_list[i]) > 0:
        lncount += int(skip_list[i])

print(final_str)


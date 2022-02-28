# You receive a string consisting of a number between two letters. For the given string, you should perform different
# mathematical operations to achieve a result:
#     • First, if the letter in front of the number is:
#         ◦ Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
#         ◦ Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
#     • Next, if the letter after the number is:
#         ◦ Uppercase: subtract its position from the resulting number (starting from 1)
#         ◦ Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping
# track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers,
# it became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and sums the final results of each

# Output
#     • Print at the console a single number:
#         ◦ The total sum of all processed numbers, formatted to the second decimal separator
# Input
# A12b s17G
# P34562Z q2576f   H456z
# a1A
import re
user_input = input()
pattern = r"\w(\d*)\w"
output = re.findall(pattern, user_input)
for num in output:
    output.index(num)


num_list = [int(x) for x in output]
print(num_list)

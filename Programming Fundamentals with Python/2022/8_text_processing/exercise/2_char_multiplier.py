# Character Multiplier
# Create a program that receives two strings on a single line separated by a single space. 
# Then, it prints the sum of their multiplied character codes as follows: 

# multiply str1[0] with str2[0] and add the result to the total sum, then continue 
# with the next two characters. 
# If one of the strings is longer than the other, add the remaining character codes
#  to the total sum without multiplication.
# import pandas as pd
# import numpy as np

user_input = input().split(' ')
sum_of_multiplied = 0
list_letter_char_sum = 0

str1 = user_input[0]
# print(len(str1))
str2 = user_input[1]
# print(len(str2))


if len(str1) > len(str2):
    rest = [ord(x) for x in str1[slice(len(str1) - len(str2))]]
    print(rest)
    restsum = sum(rest)
    str1 = str1[slice(len(str2))]
    result = sum(map(lambda x, y: ord(x) * ord(y), str1, str2)) + restsum
    
elif len(str2) > len(str1):
    rest = [ord(x) for x in str2[slice(len(str2) - len(str1))]]
    print(rest)
    restsum = sum(rest)
    str2 = str2[slice(len(str1))]
    result = sum(map(lambda x, y: ord(x) * ord(y), str1, str2)) + restsum
elif len(str1) == len(str2):
    result = sum(map(lambda x, y: ord(x) * ord(y), str1, str2))
print(result)
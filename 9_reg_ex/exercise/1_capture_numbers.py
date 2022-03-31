# 1. Capture the Numbers
# Write a program that finds all numbers in a sequence of strings.
# The output is all the numbers, extracted and printed on a single line – each separated by a single space.
import re
test = ''
input_data = input()
pattern = r'(\d+)'
matches = re.findall(pattern, input_data)
print(matches)
for match in matches:
     test += match + ' '
print(test)
#     1. Capture the Numbers
# Write a program that receives strings on different lines and extracts only the numbers. Print all extracted numbers on a single line, separated by a single space.


# Example Input
# The300
# What is that?
# I think it's the 3rd movie 
# Let's watch it at 22:45
import re
from string import digits
matches = []
user_input = " "
while user_input != "":
    user_input = input()
    pattern = r"\d+"
    output = re.findall(pattern, user_input)
    for digit in output:
        if digit != "":
            matches.append(int(digit))
    for match in matches:   
        print(match, end=" ")
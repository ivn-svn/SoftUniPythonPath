# Write a program that finds all integer and floating-point numbers in a string.
# e.g.: Input
# 1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5
import re
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
user_input = input()
matches = re.finditer(pattern, user_input)


for match in matches:
    print(match.group(0), end=" ")
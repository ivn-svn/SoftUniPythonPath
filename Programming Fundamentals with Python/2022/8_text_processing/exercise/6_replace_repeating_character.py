#     6.  Replace Repeating Chars
# Write a program that reads a string from the console and replaces any
#     sequence of the same letters with a single corresponding letter.

# Input
# aaaaabbbbbcdddeeeedssaa
# qqqwerqwecccwd
#
# Output
# abcdedsa
# qwerqwecwd
repeated = False
repeated_times = {}
user_input = input()
replacement_string = ''
counter = 0
for letter in user_input:
    if letter in replacement_string:
        if user_input.count(letter) > 1:
            if user_input[counter - 1] != letter:
                replacement_string += letter
    else:
        replacement_string += letter
    counter += 1
print(replacement_string)

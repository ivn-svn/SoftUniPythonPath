# https://judge.softuni.org/Contests/Practice/Index/2302#1
import re


def ascii_sum():
    letter_sums = []
    letter_sum = 0
    for match in matches:
        for letter in matches:
            letter_sum += ord(letter)
        letter_sums.append(letter_sum)
    return letter_sums


pattern = r"(?<=::)([A-Z][a-z][a-z]+)(?=::)|(?<=\*\*)([A-Z][a-z][a-z]+)(?=\*\*)"
output = []
user_input = input()

matches = re.finditer(pattern, user_input)

for match in matches:
    output.append(matches)


print(output)

# regex to use:

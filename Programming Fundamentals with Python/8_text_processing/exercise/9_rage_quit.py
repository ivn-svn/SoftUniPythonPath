# When P. rage-quits, he wants to be the most annoying kid on his team; he wants something
# truly spectacular. He asks for your help.
# He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N),'
#   ' e.g., "a3". You need to convert the letters to uppercase for each string and print it repeatedly N times on the '
#   'console.
#   In the example, you need to write back "AAA".
# First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the
# format: "Unique symbols used {0}".
# Next, print the rage message itself.
# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol,
# and for each string, there will be a corresponding number. The input will be given on a single line.
# Input
#     • The input data should be read from the console.
#     • It consists of a single line holding a series of string-number sequences.
#     • The input data will always be valid. There is no need to check it explicitly.
# Output
#     • The output should be printed on the console. It should consist of exactly two lines:
#         ◦ On the first line, print the number of unique symbols used in the message in the format described above.
#         ◦ On the second line, print the rage message.
import re

user_input = input()
pattern = r"([A-z])(\d)|([A-z])(\d+)|([A-z]+)(\d)|([A-z]+)(\d+)|(\D)(\d)|(\D+)(\d)|(\D)(\d+)|(\D+)(\d+)"
matches = re.findall(pattern, user_input)
letter_num_dict = {}
newstr = ""
for tup in matches:
    refined = [x for x in tup if x != ""]
    letter = refined[0]
    number = int(refined[1])
    letter_num_dict[letter] = number
for (k, v) in letter_num_dict.items():
    newstr += (k.upper() * v)
uniqs = len(list(set(newstr)))
print(f"Unique symbols used: {uniqs}")
print(newstr)

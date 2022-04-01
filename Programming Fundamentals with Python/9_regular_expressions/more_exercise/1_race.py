# Write a program that processes information about a race.
# On the first line you will be given list of participants separated by ", ".
#
# On the next few lines until you receive a line "end of race" you will be given some info
# which will be some alphanumeric characters.
#
# In between them you could have some extra characters
# which you should ignore. For example: "G!32e%o7r#32g$235@!2e". The letters are the name of the person
# and the sum of the digits is the distance he ran. So here we have George who ran 29 km.
# Store the information about the person only if the list of racers contains the name of the person.
# If you receive the same person more than once just add the distance to his old distance.
# At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"
import re

line = input()
participants_list = line.split(', ')



while line != 'end of race':
    num_pattern = r'\d+'
    letter_pattern = r'\[A-z]{1}'
    match_letters = re.findall(letter_pattern, line)
    match_nums = re.findall(num_pattern, line)
    line = input()
print(match_letters)
print(match_nums)
#
# import re
# line = input()
# num_pattern = r'\d+'
# letter_pattern = r'\[A-z]{1}'
# match_letters = re.findall(letter_pattern, line)
# match_nums = re.findall(num_pattern, line)

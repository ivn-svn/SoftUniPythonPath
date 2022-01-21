# Write a program which receives a single string. 
# On the first line it should print all the digits found in the string, on the second – 
# all the letters, and on the third – all the other characters. 
# There will always be at least one digit, one letter and one other characters.
user_input = input()
digits = ''
letters = ''
other_chars = ''
for x in user_input:
    if x.isalpha():
        letters += x
    elif x.isnumeric():
        digits += x
    else:
        other_chars += x
print(f'{digits}\n{letters}\n{other_chars}')
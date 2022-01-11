#     5. Digits, Letters and Other
# Write a program which receives a single string.
# On the first line it should print all the digits found in the string,
#     on the second – all the letters, and on the third – all the other characters.
#     0There will always be at least one digit, one letter and one other characters.
single_string = input()
letters = ''
digits = ''
etc = ''
for i in single_string:
    if i.isalpha():
        letters += i
    elif i.isdigit():
        digits += i
    else:
        etc += i
print(digits)
print(letters)
print(etc)

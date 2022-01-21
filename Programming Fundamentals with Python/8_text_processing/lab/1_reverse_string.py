# •	Reverse Strings
# You will be given series of strings until you receive an "end" command. 
# Write a program that reverses strings and prints each pair on separate line in the format "{word} = {reversed word}".
# Examples
# helLo
# Softuni
# bottle
# end
user_input = ''
str_rev_dict = {}
endloop = False
while endloop != True:
    user_input = input()
    if user_input == 'end':
        endloop = True
        break
    elif user_input != 'end':
        rev_str = user_input[::-1]
        str_rev_dict[user_input] = rev_str
for (k, v) in str_rev_dict.items():
    print(f'{k} = {v}')
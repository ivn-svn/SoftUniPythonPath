# Extract Person Information
# Write a program that reads N lines of strings and extracts the name and the age of a given person:
#     •    The person's name will be surrounded by "@" and "|" in the format "@{name}|".
#     •    The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old." 
# For each found name-age pair, print a line in the following format "{name} is {age} years old."
person_name = ''
person_age = 0
n_lines = int(input())
person_dict = {}
user_input = ''
user_inputs = []
for i in range(0, n_lines):
    user_input = input()
    #
    user_inputs.append(user_input)
# For loop to identify names:
for inp in user_inputs:
    for item in inp.split(' '):
        if '@' and '|' in item:
            person_name = item[slice(item.index('@') + 1, item.index('|'))]
            person_dict[person_name] = 0
        if '#' and '*' in item:
            person_age = item[slice(item.index('#') + 1, item.index('*'))]
            person_age = int(person_age)
            person_dict[person_name] += person_age
        #
# For loop to output the values:
for (name, age) in person_dict.items():

    print(f'{name} is {age} years old.')
# Write a program that reads N lines of strings and extracts the name and age of a given person.
# The name of the person will be between '@' and '|'. The person’s age will be between '#' and '*'.
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name and age print a line in the following format "{name} is {age} years old."
n_lines = int(input())
name = ''
age = ''
data_input = ''
input_list = []
name = []
age = []
startindexing = 0
endindexing = 0
for i in range(0, n_lines):
    data_input = input()
    for x in data_input:
        if x == "@":
            startindexing = data_input.index(x)
        elif x == "|":
            endindexing = data_input.index(x)
    name = slice(startindexing, endindexing)
    print(data_input[name])
    input_list += data_input
print(f"{name} is {age} years old.")
# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact
# by name and print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."

name = ''
number = ''
search = ''
search_items = []

phonenum = ""

person_phone_dict = {}
readline = input()
while not readline.isnumeric():
    spl0 = readline.split('-')
    name = spl0[0]
    # print(name)
    number = spl0[1]
    # print(number)
    if name not in person_phone_dict.keys():
        person_phone_dict[name] = number
    readline = input()
else:
    readline = int(readline)
    n = readline

for i in range(0, n):
    search = input()
    if search in person_phone_dict.keys():
        print(f"{search} -> {person_phone_dict[search]}")
    else:
        print(f"Contact {search} does not exist.")

# print(person_phone_dict)


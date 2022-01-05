# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists in the phonebook,
#  update its number.
# After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact by name and print
#  its details in the
#  format: "{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."

# OUTPUT:
# Contact Mery does not exist.
# Adam -> 0888080808

#phonebook = zip(name, phone)


name_lookup = []
endread = False
phonebooklist = {}


while endread == False:
    user_input = input()
    if user_input.isalnum():
        user_input.split("-")

        name = user_input[0]
        phone = user_input[1]

        phonebooklist[name] = phone


    elif user_input.isnumeric():
        for i in range(0, int(user_input)):
            nameseek = input()
            name_lookup.append(nameseek)
        for x in name_lookup:
            if x in phonebooklist:
                for (keys, values) in phonebooklist:
                    if keys in phonebooklist:
                        print(f"{keys} -> {values}")
            else:
                print(f"Contact {x} does not exist.")
        endread = True
        break
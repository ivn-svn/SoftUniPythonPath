name_lookup = []
endread = False
phonebooklist = {}


while endread == False:
    user_input = input()
    if '-' in user_input:
        user_input = user_input.split("-")

        name = user_input[0]
        phone = user_input[1]

        phonebooklist[name] = phone


    elif user_input.isdigit():
        for i in range(0, int(user_input)):
            nameseek = input()
            name_lookup.append(nameseek)
        for x in name_lookup:
            if x in phonebooklist:
                for (keys, values) in phonebooklist.items():
                    if keys in phonebooklist:
                        print(f"{keys} -> {values}")
            else:
                print(f"Contact {x} does not exist.")
        endread = True
        break
name_lookup = []
endread = False
phonebooklist = {}
counter = 0


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


        for (keys, values) in phonebooklist.items():
            if keys in name_lookup:
                print(f"{keys} -> {values}")
                counter += 1
            elif name_lookup[counter] not in phonebooklist.items():
                print(f"Contact {name_lookup[counter]} does not exist.")
                counter += 1
        # for zz in name_lookup:
        #     if zz not in phonebooklist:
        #         print(f"Contact {zz} does not exist.")
        endread = True
        break
first_sub = ''
second_sub = ''
comidx = 0
data_input = input()
while True:
    command = input()
    com = command.split(" ")
    if com == "For Azeroth":
        break
    elif "GladiatorStance" in com:
        data_input = data_input.upper()
        print(data_input)
    elif  "DefensiveStance" in com:
        data_input = data_input.lower()
        print(data_input)
    elif "Dispel" in com:
        try:
            comidx = com.index("Dispel")
            "Dispel".replace(com[comidx + 1], com[comidx + 2])
            print("Success!")
        except IndexError:
            print("Dispel too weak.")
    elif "Target Change" in com:
        comidx = com.index("Target Change")
        first_sub = com[comidx + 1]
        second_sub = com[comidx + 2]
        # for every instance of the first change to second
        for first in range(0, len(data_input)):
            if data_input[first] in first_sub:
                data_input[first].replace(first_sub[first], second_sub[first])
        print(data_input)
    elif "Target Remove" in com:
        try:
            comidx = com.index("Target Remove")
            data_input.remove(com[comidx + 1])
            print(data_input)
        except ValueError:
            print("Command doesn't exist!")
    # else:
    #     print("Command doesn't exist!")

first_sub = ''
second_sub = ''
while True:
    command = input()
    if command == "For Azeroth":
        break
    elif command == "GladiatorStance":
        command = command.upper()
    elif command == "DefensiveStance":
        command = command.lower()
    elif "Dispel" in command.split(" "):
        try:
            co = command[0]
            command[0].replace(co[int(command[1])], command[2])
            print("Success!")
        except IndexError:
            print("Dispel too weak.")
    elif "Change" in command.split():
        first_sub = command[2]
        second_sub = command[3]
    elif "Remove" in command.split():
        command.split().remove(command[2])
    else:
        print("Command doesn't exist!")

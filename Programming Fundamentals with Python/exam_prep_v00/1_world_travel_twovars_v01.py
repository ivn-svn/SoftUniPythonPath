initial_string = input()
#
final_string = initial_string
end_cycle = False


def perform_action(cmd, final_str):
    cmd_split = cmd.split(':')
    if 'add' in cmd_split[0].lower():
        index = int(cmd_split[1])
        stop_name = cmd_split[2]
        if index <= len(final_str):
            frontpart = final_str[:index]
            backpart = final_str[index:]
            final_str = frontpart + stop_name + backpart
    elif 'remove' in cmd_split[0].lower():
        index = int(cmd_split[1])
        index1 = int(cmd_split[2]) + 1
        if index and index1 <= len(final_str):
            iten = final_str[index:index1]
            final_str = final_str.replace(iten, '')
    elif 'switch' in cmd_split[0].lower():  # TODO: finish the switch func
        old = cmd_split[1]
        new = cmd_split[2]
        if old in final_str:
            final_str = final_str.replace(old, new)

    return final_str


command = ''
commands = []

#
while command != "Travel" and end_cycle == False:
    command = input()
    if command != "Travel":
        commands.append(command)
        final_string = perform_action(command, final_string)
        print(final_string)
    elif command == "Travel":
        end_cycle = True



else:
    print(f"Ready for world tour! Planned stops: {final_string}")

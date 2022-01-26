
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#0.
#
# You are a world traveler, and your next goal is to make a world tour. To do that, you have to plan out everything first.
#  To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel", 
# you will be given some commands to manipulate that initial string. The commands can be:
# "Add Stop:{index}:{string}":
# Insert the given string at that index only if the index is valid
# "Remove Stop:{start_index}:{end_index}":
# Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# "Switch:{old_string}:{new_string}":
# If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
initial_string = input()
#
def perform_action(cmd, stp_lst):
    cmd_split = cmd.split(':')
    if 'add' in cmd_split[0].lower():
        index = int(cmd_split[1])
        stop_name = cmd_split[2]
        if index <= len(stp_lst):
            stp_lst.insert(index, stop_name)
    elif 'remove' in cmd_split[0].lower():
        index = int(cmd_split[1])
        index1 = int(cmd_split[2])
        if index and index1 <= len(stp_lst):
            pop_items = stp_lst[index:index1]
            for item in pop_items:
                stp_lst.pop(item)        
    elif 'switch' in cmd_split[0].lower():
        old = cmd_split[0]
        new = cmd_split[1]
        if old in stp_lst:  
            old_overwrite = stp_lst.index(old)
            new_overwrite = stp_lst.index(new)
            if old_overwrite and new_overwrite <= len(stp_lst):  
                stp_lst[old_overwrite] = stp_lst[new_overwrite]
    return stp_lst
command = ''
commands = []
stops_list = []
while command != "Travel":
    command = input()
    commands = stops_list.append(command)
    stops_list = perform_action(command, stops_list)
    print(stops_list)

else:
    print(f"Ready for world tour! Planned stops: ")
# Reworking vars:
# line = 'Kong Panda'
# index = line.find('Panda')
# output_line = line[:index] + 'Fu ' + line[index:]
# output_line
#
initial_string = input()
#
final_string = initial_string
def perform_action(cmd, stp_lst, init_str, final_str):
    cmd_split = cmd.split(':')
    if 'add' in cmd_split[0].lower():
        index = int(cmd_split[1])
        stop_name = cmd_split[2]
        if index <= len(init_str):
            # stp_lst.insert(index, stop_name)
            # Reworking the above:
            final_str = final_str[:index] + stop_name + final_str[index:]
    elif 'remove' in cmd_split[0].lower():
        index = int(cmd_split[1])
        index1 = int(cmd_split[2])
        if index and index1 <= len(final_str):
            # pop_items = stp_lst[index:index1]
            # Reworking the above:
            final_str = final_str[:index] + final_str[index:]
            # for item in pop_items:
            #     stp_lst.pop(item)        
    elif 'switch' in cmd_split[0].lower(): #TODO: finish the switch func 
        old = cmd_split[0]
        new = cmd_split[1]
        if old in final_str:  
            # old_overwrite = stp_lst.index(old)
            # new_overwrite = stp_lst.index(new)
            final_str.replace(old, new)  
                
    return final_str
command = ''
commands = []
stops_list = ''
while command != "Travel":
    command = input()
    commands = stops_list.append(command)
    stops_list = perform_action(command, stops_list, initial_string, final_string)
    print(stops_list)

else:
    print(f"Ready for world tour! Planned stops: {stops_list}")
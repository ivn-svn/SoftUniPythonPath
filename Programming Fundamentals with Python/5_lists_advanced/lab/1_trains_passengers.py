# You will receive how many wagoons the train has. Create a list with that length
# with all zeros. Until you receive the command "End", you get some of the following commands:
#     • add {people} -> adds the people in the last wagon
#     • insert {index} {people} -> adds the people at the given wagon
#     • leave {index} {people} -> removes the people from the wagon
# After you receive the "End" command print the train
n = int(input())
command = ''
wagoons = [0]
command_list = []
editedvalue = 0
for x in range(1, n + 1):
    wagoons.append(0)
while command.lower() != 'end':
    command = input()
    command_list = command.split(' ')
    if command_list[0] == "add":
        editedvalue = int(command_list[1])
        wagoons.append(editedvalue)
    elif command_list[0] == "insert":
        index = int(command_list[1])
        editedvalue = int(command_list[2])
        wagoons[index] += editedvalue
    elif command_list[0] == "leave":
        index = int(command_list[1])
        editedvalue = int(command_list[2])
        wagoons[index] -= editedvalue
        #
print(wagoons)
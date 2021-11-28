n = int(input())
wagons = [0] * n
# wagons_list = []
command = input()
while command != 'End':
    #
    tokens = command.split(' ')
    commanda = tokens[0]
    passengers = tokens[1]
#
    if command == 'Add':
        wagons[len(wagons)] += passengers
    elif command == 'Insert':
        commanda = tokens[0]
        index = int(tokens[1])
        passengers = int(tokens[2])
        wagons[index] += passengers
    elif command == 'Leave':
        commanda = tokens[0]
        index = int(tokens[1])
        passengers = int(tokens[2])
        wagons[index] -= passengers
print(wagons)


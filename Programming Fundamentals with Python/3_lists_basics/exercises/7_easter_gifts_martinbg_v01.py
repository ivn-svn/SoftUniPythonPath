gifts = input().split()

command = input()
while command != 'No Money':
    tokens = command.split()
    command = tokens[0]
    gift = tokens[1]

    if command == 'OutOfStock':
        for index, current_gift in enumerate(gifts): # index is integer while current_gift is the element
            # we'll be searching for within the gifts list.
            if current_gift == gift:
                gifts[index] = 'None'

    elif command == 'Required':
        index = int(tokens[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif command == 'JustInCase':
        gifts[-1] = gift # takes the last element from the gifts list.

    command = input()

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))

cmd = ''
# list of possible commands
add = 'Add'
remove = 'Remove'
removeat = 'Remove At'
insert = 'Insert'

cards = input().split(', ')
num_cards = int(input())
#
# cards_list
card_name = ''

for i in range(0, num_cards):
    cmd = input()
    cmd_split = cmd.split(', ')
    if add in cmd_split:
        card_name = cmd_split[1]
        if card_name in cards:
            print(f"Card is already in the deck")
        elif card_name not in cards:
            cards.append(card_name)
            print(f"Card successfully added")
    #
    elif remove in cmd_split:
        card_name = cmd_split[1]
        if card_name in cards:
            cards.remove(card_name)
            print(f"Card successfully removed")
        elif card_name not in cards:
            print(f"Card not found")
    #
    elif removeat in cmd_split:
        index = int(cmd_split[1])
        if len(cards) > index >= 0:
            card_name = cards[index]
            if card_name in cards:
                cards.remove(card_name)
                print(f"Card successfully removed")
            elif card_name not in cards:
                print(f"Card not found")
        else:
            print("Index out of range")

    elif insert in cmd_split:
        #
        index = int(cmd_split[1])
        if index >= 0:
            card_name = cmd_split[2]
            cards.insert(index, card_name)
            print(f"Card successfully added")
        else:
            print("Index out of range")

print(', '.join(cards))
# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts
# you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
#     • "OutOfStock {gift}"
#         ◦ Find the gifts with this name in your collection, if any, and change their values to "None".
#     • "Required {gift} {index}"
#         ◦ If the index is valid, replace the gift on the given index with the given gift.
#     • "JustInCase {gift}"
#         ◦ Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None",
# separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
#     • On the 1st line,  you will receive the names of the gifts, separated by a single space.
#     • On the following lines, until the "No Money" command is received, you will be receiving commands.
#     • The input will always be valid.
# Output
#     • Print the gifts in the format described above.
gifts = input().split(' ')
commands = input().split(' ')
gift = ''


def cmd_analyzer(cmd):
    if len(cmd) == 2:
        if cmd[0] == 'OutOfStock':
            gifts.replace(cmd[1], 'None')
        elif cmd[0] == 'JustInCase':
            gifts[len(gifts) - 1] = cmd[1]
    elif len(cmd) == 3:
        if cmd[0] == 'Required': # check if is required
            gifts.replace(gifts[cmd[1]], cmd[0])


while commands != 'No Money':
    commands = input().split(' ')
    gifts = cmd_analyzer(commands)
else:
    finalgiftslist = [g for g in gifts if g != 'None']
print(finalgiftslist)

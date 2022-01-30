# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#0.
#
# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code. '
#
#                                                 'Your job is to create a program to crack the codes.
#
#
# On the first line of the input, you will receive the encrypted message. After that, until the "Decode"
# command is given, you will be receiving strings with instructions for different operations that need to be
# performed upon the concealed message to interpret it and reveal its true content. There are several types of
# instructions, split by '|'
# "Move {number of letters}":
# Moves the first n letters to the back of the string
# "Insert {index} {value}":
# Inserts the given value before the given index in the string
# "ChangeAll {substring} {replacement}":
# Changes all occurrences of the given substring with the replacement text
#
# Functions to decode the message:
def decode_func(cmd, act, msg):
    global message

    if act == "ChangeAll":
        replacable = cmd[1]
        replacement = cmd[2]
        message = message.replace(replacable, replacement)
    elif act == "Insert":
        idx = int(cmd[1])
        value = str(cmd[2])
        message = message[:idx] + value + message[idx:]
    elif act == "Move":
        movement = int(cmd[1])
        movable = slice(0, movement)
        movable = message[movable]
        message = message.replace(movable, '')
        message = message + movable
    return message


encr_message = input()
end = False
message = encr_message
while end == False:
    commands = input().split('|')
    if "Decode" in commands:
        end = True
        break
    else:
        action = commands[0]

        message = decode_func(commands, action, message)

print(f"The decrypted message is: {message}")
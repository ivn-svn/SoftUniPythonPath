# Text Filter
# Write a program which receives a text and a string of banned words, separated by a comma and space ", ". 
# All words included in the ban list should be replaced with asterisks "*", equal to the word's length. 
# The ban list will be entered on the first input line and the text - on the second input line. 
# Input:
# Linux, Windows
# It is not Linux, it is GNU/Linux. Linux is merely the kernel, while GNU adds the functionality. 
# Therefore we owe it to them by calling the OS GNU/Linux! Sincerely, a Windows client

# Output:
# It is not *****, it is GNU/*****.
#  ***** is merely the kernel, while GNU adds the functionality. 
#  Therefore we owe it to them by calling the OS GNU/*****! Sincerely, a ******* client
words_to_ban = input().split(', ')
text = input()
banlist = {}
for x in words_to_ban:
    banlist[x] = ('*' * len(x))
for keys, values in banlist.items():
    text = text.replace(keys, values)
print(text)


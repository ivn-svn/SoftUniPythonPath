# Write a program that reads usernames on a single line (separated by ", ")
# and prints all valid usernames on separate lines.
# A valid username:
#     • has length between 3 and 16 characters inclusive
#     • can contain only letters, numbers, hyphens, and underscores
#     • has no redundant symbols before, after, or in between
length_upper = 16
length_lower = 3
special_s_restrictions = '_-'
usernames = input().split(', ')
validusernames = []
for username in usernames:
    special_ch = False
    for x in special_s_restrictions:
        if x in username:
            special_ch = True
    if username.isalnum() and 16 >= len(username) >= 3 and ' ' not in username or special_ch is True:
        validusernames.append(username)
    special_ch = False
for z in validusernames:
    print(z)

# The force users struggle to remember which side is the different force users from because they switch them too
# often. So you are tasked to create a web application to manage their profiles. You should store information for
# every unique force user registered in the application. You will receive several input lines in one of the following
# formats: "{force_side} | {force_user}" "{force_user} -> {force_side}" The "force_user" and "force_side" are
# strings, containing any character.
#
# If you receive "force_side | force_user": • If there is no such force user and
# no such force side -> create a new force side and add the force user to the corresponding side. • Only if there is
# no such force user in any force side -> add the force user to the corresponding side. • If there is such force user
# already -> skip the command and continue to the next operation. If you receive a "force_user -> force_side": • If
# there is such force user already -> change their side. • If there is no such force user in any force side -> add
# the force user to the corresponding force side. • If there is no such force user and no such force side -> create
# new force side and add the force user to the corresponding side. • Then you should print on the console: "{
# force_user} joins the {force_side} side!". You should end your program when you receive the command "Lumpawaroo".
# At that point, you should print each force side. For each side, print the force users. In case there are no force
# users on a side, you shouldn't print the side information. Input / Constraints • The input comes in the form of
# commands in one of the formats specified above. • The input ends when you receive the command "Lumpawaroo". Output
# • As output for each force side, you must print all the force users. • The output format is: "Side: {force_side},
# Members: {force_users_count} ! {force_user1} ! {force_user2} … ! {force_userN}" • In case there are NO force users
# on a side, don't print this side.

cmd = input()
force_side = ''
force_user = ''
side_user_dictionary = dict()


def getkey_by_val(sud, s_item):  # a func to search and pop values: actually pop users
    for (k, v) in sud.items():
        if s_item in v:
            found = v.index(s_item)
            sud[k].pop(found)
            break
    return sud


def switch_sides(user, side, sud, signal):
    list_all_vals = []
    for tup in sud.values():
        for vals in tup:
            list_all_vals.append(vals)
    if signal == "|":
        if user not in list_all_vals and side not in sud.keys():
            sud[side] = []
            sud[side].append(user)
        elif side in sud.keys() and user not in list_all_vals:
            sud[side].append(user)
        elif user in list_all_vals:
            pass
    elif signal == "->":
        if user in list_all_vals:
            search_val = user
            sud = getkey_by_val(sud, search_val)
            sud[side].append(user)
            print(f"{user} joins the {side} side!")
        elif user not in list_all_vals and side not in sud.keys():
            sud[side] = []
            sud[side].append(user)
            print(f"{user} joins the {side} side!")
        elif side in sud.keys() and user not in list_all_vals:
            sud[side].append(user)
            print(f"{user} joins the {side} side!")
    return sud


def printable_func(sud):
    for (side,user) in sud.items():
        side_len = len(sud[side])
        if side_len == 0:
            pass
        else:
            print(f"Side: {side}, Members: {side_len}")
        for person in user:
            print(f"! {person}")


while cmd != "Lumpawaroo":

    if "|" in cmd:
        cmd_split = cmd.split(" | ")
        force_user = cmd_split[1]
        force_side = cmd_split[0]
        signal_char = "|"
        # add function
        side_user_dictionary = switch_sides(force_user, force_side, side_user_dictionary, signal_char)
    elif "->" in cmd:
        cmd_split = cmd.split(" -> ")
        force_user = cmd_split[0]
        force_side = cmd_split[1]
        signal_char = "->"
        # add function
        side_user_dictionary = switch_sides(force_user, force_side, side_user_dictionary, signal_char)

    cmd = input()
else:
    printable_func(side_user_dictionary)

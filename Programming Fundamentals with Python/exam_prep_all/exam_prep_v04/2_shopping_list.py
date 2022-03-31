# # https://judge.softuni.org/Contests/Practice/Index/2031#1
# Input
# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
#     • "Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
#     • "Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise,
# skip this command.
#     • "Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one.
# Otherwise, skip this command.
#     • "Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the
# end of the list. Otherwise, skip this command.
initial_list = input().split("!")
command = ""
grocery_list = initial_list


def urgent(ilst, cm):
    if len(cm) == 2:
        item = cm[1]
    else:
        item = ''
    listlen = len(ilst)
    if item not in ilst and item not in ["", " "] and listlen != 0:
        ilst.insert(0, item)
    return ilst


def unnecessary(ilst, cm):
    if len(cm) == 2:
        item = cm[1]
    else:
        item = ''
    listlen = len(ilst)
    if item in ilst and listlen != 0:
        ilst.pop(item)

    return ilst


def correct(ilst, cm):
    if len(cm) == 3:
        item = cm[1]
    else:
        item = ''
    new_item = cm[2]
    listlen = len(ilst)
    if item in ilst and listlen != 0:
        item_idx = ilst.index(item)
        ilst[item_idx] = new_item

    return ilst


def rearrange(ilst, cm):
    if len(cm) == 2:
        item = cm[1]
    else:
        item = ''
    listlen = len(ilst)
    if item in ilst and listlen != 0:
        ilst.pop(item)
        ilst.append(item)

    return ilst


command = input()
while command != "Go Shopping!":
    cmd = command.split(" ")
    if "Urgent" in cmd:
        grocery_list = urgent(grocery_list, cmd)
    elif "Unnecessary" in cmd:
        grocery_list = unnecessary(grocery_list, cmd)
    elif "Correct" in cmd:
        grocery_list = correct(grocery_list, cmd)
    elif "Rearrange" in cmd:
        grocery_list = rearrange(grocery_list, cmd)
    command = input()

grocery_list_joined = ", ".join(grocery_list)
print(f"{grocery_list_joined}")

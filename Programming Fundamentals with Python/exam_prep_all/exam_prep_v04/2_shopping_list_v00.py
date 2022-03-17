def urgent(journal, item):
    if item not in journal:
        journal.insert(0, item)
    return journal


def unnecessary(journal, item):
    if item in journal:
        journal.remove(item)
    return journal


def correct(journal, items):
    [old_item, new_item] = items.split()
    for i in range(len(journal)):
        if journal[i] == old_item:
            journal[i] = new_item
    return journal


def rearrange(journal, item):
    for i in range(len(journal)):
        if journal[i] == item:
            journal.remove(item)
            journal.extend(item)
    return journal


initial_list = input().split("!")

commands = input()

while commands != "Go Shopping!":
    [command, item] = commands.split(' ', 1)
    if command == "Urgent":
        initial_list = urgent(initial_list, item)
    elif command == "Unnecessary":
        initial_list = unnecessary(initial_list, item)
    elif command == "Correct":
        initial_list = correct(initial_list, item)
    elif command == "Rearrange":
        initial_list = rearrange(initial_list, item)

    commands = input()

print(", ".join(initial_list))

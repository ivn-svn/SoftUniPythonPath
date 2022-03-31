# https://judge.softuni.org/Contests/Practice/Index/2028#2
journal_collectible_items = [item for item in input().split(", ")]
actions = ""
while actions != "Craft!":
    if actions == "Craft":
        break
    elif actions != "Craft" and actions != "":
        cmd = actions.split(" - ")[0]
        item = actions.split(" - ")[1]
        if cmd == "Collect":
            if item in journal_collectible_items:
                pass
            else:
                journal_collectible_items.append(item)
        elif cmd == "Drop":
            if item in journal_collectible_items:
                journal_collectible_items.remove(item)
        elif cmd == "Combine Items":
            old_item = item.split(":")[0]
            new_item = item.split(":")[1]
            if old_item in journal_collectible_items:
                idx = journal_collectible_items.index(old_item) + 1
                journal_collectible_items.insert(idx, new_item)
        elif cmd == "Renew":
            if item in journal_collectible_items:
                journal_collectible_items.remove(item)
                journal_collectible_items.append(item)
    actions = input()
printable = ", ".join(journal_collectible_items)
print(printable)
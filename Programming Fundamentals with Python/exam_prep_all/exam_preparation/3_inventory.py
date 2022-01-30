# https://judge.softuni.bg/Contests/Practice/Index/2028#2
# You will receive a journal with some Collecting items, separated with ", " (comma and space).
# After that, until receiving "Craft!" you will be receiving different commands.
# Commands (split by " - "):
# "Collect - {item}" – Receiving this command, you should add the given item in your inventory.
# If the item already exists, you should skip this line.
# "Drop - {item}" – You should remove the item from your inventory, if it exists.
# "Combine Items - {oldItem}:{newItem}"
#
# – You should check if the old item exists, if so, add the new item after the old one.
# Otherwise, ignore the command.
# "Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.
# true_check = True  # Starting a while loop which should run until the "Craft!" command would reset the value of the
# "true_check" variable to "False", so that the loop would stop collecting, removing and renewing items.
while True:
    collect_items = input().split(", ") # variable to hold the input elements
    # separated from each other based on ", "
    separated_collection = []  # variable to hold the input elements separated from each other based on " - "
    edited_collection = []  # variable to hold the elements needed for the output
    splited_dots = [] # variable to hold the list values after spliting separated_collection by ":"
    combo = []
    for z in collect_items.split(" - "):
        separated_collection += z
        #
        # for x in separated_collection:
        if "Craft!" in z.split(" - "):
            print(edited_collection)
            break
        elif "Drop" in z:
            edited_collection = collect_items.remove(z)
        elif "Combine Items" in z:
            splited_dots = h.split(":")  # separates combo in to two elements divided by :
            combo = [y for y in z if ":" in splited_dots]  # puts the items from the element containing "Combine Items"
            # in a single variable
            for h in combo:
                edited_collection = separated_collection.insert(len(z), splited_dots[1])  #
            # adds only the neccessary elements to the final output variable.
        elif "Renew" in z:
            #
            edited_collection = edited_collection.remove(z)  # renews the element by removing it
            edited_collection = edited_collection.append(z)  # and inserting the new element.
# Example input:
# Iron, Wood, Sword
# Collect - Gold
# Drop - Wood
# Craft!

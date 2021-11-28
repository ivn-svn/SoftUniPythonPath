# You will receive a journal with some Collecting items, separated with ', ' (comma and space).
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
true_check = True  # Starting a while loop which should run until the "Craft!" command would reset the value of the
# "true_check" variable to "False", so that the loop would stop collecting, removing and renewing items.
while true_check:
    collect_items = str(input()).split(', ')  # # variable to hold the input elements
    # separated from each other based on ", "
    separated_collection = []  # variable to hold the input elements separated from each other based on " - "
    for z in collect_items:
        separated_collection += z.split(" - ")
        #
        for x in separated_collection:
            if 'Craft!' in separated_collection:
                true_check = False
                print(f'{separated_collection}')
                break
            elif 'Drop' in separated_collection:
                separated_collection.remove(z)
            elif 'Combine Items' in separated_collection:
                combo = [y for y in z if ':' in z]  # puts the items from the element containing "Combine Items"
                # in a single variable
                splited_dots = combo.split(':')  # separates combo in to two elements divided by :
                separated_collection.insert(len(z), splited_dots[1])  #
                # adds only the neccessary elements to the final output variable.
            elif 'Renew' in separated_collection:
                #
                edited_collection = separated_collection.remove(z)  # renews the element by removing it
                edited_collection = separated_collection.append(z)  # and inserting the new element.

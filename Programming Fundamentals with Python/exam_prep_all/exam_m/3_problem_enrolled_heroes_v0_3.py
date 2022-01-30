what_to_do = ''
hero_name = ''
hero_collection = {}
spell_book = []
command = ""
list_length = 0

while True:
    command = input()
    command = command.split(" ")
    if command[0] == "End":
        break
    else:
        what_to_do = command[0]
        hero_name = command[1]
    if what_to_do == "Enroll":
        if hero_name in hero_collection:
            print(f"{hero_name} is already enrolled.")
        else:
            hero_collection[hero_name] = []
    elif what_to_do == "Learn":
        spell = command[2]
        if hero_name in hero_collection and spell not in hero_collection[hero_name]:
            hero_collection[hero_name] += spell
        elif hero_name not in hero_collection:
            print(f"{hero_name} doesn't exist.")
        elif hero_name in hero_collection and spell in hero_collection[hero_name]:
            print(f"{hero_name} has already learnt {spell}.")
    elif what_to_do == "Unlearn":
        spell = command[2]
        if hero_name in hero_collection and spell in hero_collection[hero_name]:
            hero_collection[hero_name].remove(spell)
        elif hero_name not in hero_collection:
            print(f"{hero_name} doesn't exist.")
        elif hero_name in hero_collection and spell not in hero_collection[hero_name]:
            print(f"{hero_name} doesn't know {spell}.")
print("Heroes:")
print(f"== {' '.join(sorted(hero_collection, key=lambda k: len(hero_collection[k]), reverse=True))}")


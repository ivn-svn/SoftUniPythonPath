# Create a program that keeps track of enrolled heroes and their collection of spells (spellbook). You will
# be receiving the following commands until you receive the command "End":
# "Enroll {HeroName}":
# Learn {HeroName} {SpellName}":
# Unlearn {HeroName} {SpellName}":
# After you receive the "End" command, printall the heroes sorted by their count of spells in descending and then by the
# hero name ascending in the format described below.

hero_collection = []
spell_book = []
command = ''
hero_name = ''
spell_name = ''
sortout = []                                        #               List to contain the sorted output.
while command != "End":
    command = input()
    what_to_do = command[0]
    hero_name = command[1]
    if what_to_do.lower() == "enroll":
        if hero_name in hero_collection:
            print(f"{hero_name} is already enrolled.")
        else:
            hero_collection.append(hero_name)
        #hero_collection[hero_name] = spell_name
    if what_to_do.lower() == "learn": # If                                  L E A R N
        spell_name = command[2]                     # Learn if does not need the heroe exists message.
        if hero_name in hero_collection and spell_name in spell_book:
            print(f"{hero_name} has already learnt {spell_name}")
        elif hero_name not in hero_collection:
            print(f"{hero_name} doesn't exist.")
            hero_collection.append(hero_name)
        elif hero_name in hero_collection and spell_name not in spell_book:
            spell_book.append(spell_name)
    if what_to_do.lower() == "unlearn": # If                               U N L E A R N
        if hero_name not in hero_collection: #
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in spell_book:
            print(f"{hero_name} doesn't know {spell_name}")
        elif hero_name in hero_collection and spell_name in spell_book:
            spell_name.remove(command[2])
# To do:
# 1. Merge lists in to dictionary
# 2. sort out the output
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
    what_to_do = command[0]
    hero_name = command[1]
    if what_to_do == "Enroll":
        if hero_name in hero_collection:
            print(f"{hero_name} is already enrolled.")
        else:
            hero_collection[hero_name] = []
    if what_to_do == "Learn":
        spell = command[2]
        spell_book = hero_collection[hero_name]
        if hero_name in hero_collection and spell not in spell_book:
            spell_book.append(spell)
        elif hero_name not in hero_collection:
            print(f"{hero_name} doesn't exist.")
        elif hero_name in hero_collection and spell in spell_book:
            print(f"The {hero_name} has already learnt  {spell}")
    if what_to_do == "Unlearn":
        spell = command[2]
        spell_book = hero_collection[hero_name]
        if hero_name in hero_collection and spell in spell_book:
            spell_book.remove(spell)
        elif hero_name not in hero_collection:
            print(f"{hero_name} doesn't exist.")
        elif hero_name in hero_collection and spell not in spell_book:
            print(f"{hero_name} doesn't know {spell}")
for hero in hero_collection:
    list_length = len(hero_collection[hero])
    print(list_length)
hero_collection = dict(sorted(hero_collection.items(), key=lambda el: (-el[1], el[0])))
print(hero_collection)

# for k in sorted(d, key=lambda k: len(d[k]), reverse=True):
#         print k,
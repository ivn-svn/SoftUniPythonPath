from collections import deque


def addToDict(dct, key):
    if key in dct:
        dct[key] += 1
    else:
        dct[key] = 1
    return dct


# input1 = "20 10 40 70 20"
# input2 = "10 50 10 30 20 80"
input1 = input()
input2 = input()

textiles = deque([int(z) for z in input1.split(" ")])  
medicaments = [int(y) for y in input2.split(" ")]

inventory = {'Patch': 30, 'Bandage': 40, 'MedKit': 100}
created_items = {}

sumisindict = lambda d, x: [k for k, v in d.items() if v == x]

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    sum_textile_medicament = textile + medicament
    
    if sum_textile_medicament in inventory.values():
        listofkeys = sumisindict(inventory, sum_textile_medicament)
        for key in listofkeys:
            created_items = addToDict(created_items, key)
    
    elif sum_textile_medicament > inventory["MedKit"]:
        created_items = addToDict(created_items, "MedKit")
        difference = (textile + medicament) - inventory["MedKit"]
        medicaments[-1] += difference
    
    elif sum_textile_medicament not in inventory.values():    
        medicament += 10
        medicaments.append(medicament)

created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
created_items = dict(created_items)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
else:
    if not textiles:
        print("Textiles are empty.")
    elif not medicaments:
        print("Medicaments are empty.")

for item, count in created_items.items():
    print(f"{item} - {count}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

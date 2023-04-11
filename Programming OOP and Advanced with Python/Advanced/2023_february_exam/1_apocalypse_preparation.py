from collections import deque


def addToDict(dct, key):
    if key in dct.keys():
        dct[key] += 1
    else:
        dct[key] = 1
    return dct


# textiles = deque([int(z) for z in input().split(" ")])  

# medicaments = [int(y) for y in input().split(" ")]

# input1 = "30 30 10 80 60"
# input2 = "40 20 30 10 70"

input1 = "20 10 40 70 20"
input2 = "10 50 10 30 20 80"

# input1 = "30 30 10 80 60 20"
# input2 = "40 20 30 10 70"

# input1 = "60 15 20 30 20"
# input2 = "20 15 40"

# input1 = "20 10 40 70 20"
# input2 = "10 50 10 30 20 80" 


textiles = deque([int(z) for z in input1.split(" ")])  

medicaments = [int(y) for y in input2.split(" ")]

inventory = {'Patch': 30, 'Bandage': 40, 'MedKit': 100}

created_items = {}

sumisindict = lambda d, x: [k for k, v in d.items() if v == x]


while textiles and medicaments:
    textile = textiles.popleft() # first value of textile
    medicament = medicaments.pop() # the last value of medicaments:
    sum_textile_medicament = textile + medicament
    if sum_textile_medicament in inventory.values():
        listofvals = sumisindict(inventory, sum_textile_medicament)
        for sv in listofvals:
            created_items = addToDict(created_items, sv)
    elif sum_textile_medicament > inventory["MedKit"]:
        created_items = addToDict(created_items, inventory["MedKit"])
        difference = (textile + medicament) - inventory["MedKit"]
        medicaments[-1] += difference
    elif sum_textile_medicament not in inventory.values():    
        medicament += 10
        medicaments.append(medicament)


#created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))


print(created_items)
print(textiles)
print(medicaments)

deck = input().split(' ')
n = int(input())

for i in range(n):
    firsthalf = []
    secondhalf = []
    finallist = []

    for x in range(len(deck) // 2):
        firsthalf.append(deck[x])
    for y in range(len(deck) // 2, len(deck)):
        secondhalf.append(deck[y])
    for z in range(len(firsthalf)):
        finallist.append(firsthalf[z])
        finallist.append(secondhalf[z])
    deck = finallist
print(deck)
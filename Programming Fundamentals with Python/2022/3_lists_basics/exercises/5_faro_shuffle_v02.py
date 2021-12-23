# Input
# a b c d e f g h
# 5
# Output
# ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']

deck = input().split(" ")
num = int(input())
for i in range(num):
    firsthalf = [deck[x] for x in range(0, len(deck) // 2)]
    secondhalf = [deck[y] for y in range(len(deck) // 2, len(deck))]
    finaldeck = []
    for z in range(len(firsthalf)):
        finaldeck.append(firsthalf[z])
        finaldeck.append(secondhalf[z])
print(finaldeck)


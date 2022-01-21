deck = list(input().split(' '))
n = int(input())
#
odds = []
evens = []
newdeck = []

for i in range(1, n):
    if len(deck) % 2 == 0:
        for i in range(1, len(deck) - 1):
            if i % 2 == 0:
                evens.append(deck[i])
            else:
                odds.append(deck[i])
newdeck = [i for j in map(None, odds, evens)
           for i in j if i is not None]
# newdeck = odds + evens
# newdeck[::2] = odds
# newdeck[1::2] = evens
newdeck.insert(0, deck[0])
newdeck.append(deck[len(deck) - 1])
print(newdeck)
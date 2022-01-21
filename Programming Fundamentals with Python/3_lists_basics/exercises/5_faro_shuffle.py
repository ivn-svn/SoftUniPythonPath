# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card
# is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives
# ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second
# line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.
deck = list(input().split(' '))
newlist = []
print(deck)
odds = []
evens = []

# def countList(odds, evens):
#     return [sub[item] for item in range(len(evens))
#                       for sub in [odds, evens]]
#
if len(deck) % 2 == 0:
    for i in range(1, len(deck) -1):
        if i % 2 == 0:
            evens.append(deck[i])
        else:
            odds.append(deck[i])
print(evens)
print(odds)

# newlist = countList(odds, evens)
newlist = evens + odds
print(newlist)

newlist.insert(0, deck[0])
#newlist.insert(len(deck) - 1, deck[len(deck) - 1])
newlist.append(deck[len(deck) - 1])

print(newlist)

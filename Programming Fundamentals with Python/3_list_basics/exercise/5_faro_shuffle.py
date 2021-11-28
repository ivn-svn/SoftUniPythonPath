# # FARO SHUFFLE
# A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards
# in the two halves are perfectly interwoven, such that the original bottom card is still on the
# bottom and the original top card is still on top.
# For example, faro shuffling the list
# ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six' ]
# Write a program that receives a single string (cards separated by a space) and on the second line receives a number
# of faro shuffles that have to be made. Print the state of the deck after the shuffle
# Note: The length of the deck of cards will always be an even number
import itertools
deck_sate = input().split(" ")
frequency = int(input())
deck_state = []
#
cards_length = len(deck_sate)
first = deck_sate[0]
dsplteven = []
dspltodd = []
last = deck_sate[cards_length - 1]

#
for i in range(frequency):
    dsplteven.clear()
    dspltodd.clear()
    for enum in range(1, len(deck_sate) - 1):
        #deck_state.append(deck_sate[enum])
        if enum % 2 != 0:
            dsplteven.append(deck_sate[enum])
        else:
            dspltodd.append(deck_sate[enum])
    deck_state = list(itertools.chain(dspltodd, dsplteven))
    deck_state.insert(0, first)
    deck_state.append(last)
print(deck_state)

import itertools
card_real_input = input().split(", ")
deck_state = []
#
cards_length = len(card_real_input)
first = card_real_input[0]
last = card_real_input[cards_length -1]
dsplteven = []
dspltodd = []

#
for enum in range(1, cards_length - 1):
    deck_state.append(card_real_input[enum])
    if enum % 2 == 0:
        dsplteven.append(card_real_input[enum])
    else:
        dspltodd.append(card_real_input[enum])
deck_state = list(itertools.chain(first, dspltodd, dsplteven, last))
print(deck_state)
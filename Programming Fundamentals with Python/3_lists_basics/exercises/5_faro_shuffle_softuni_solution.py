# Input
# a b c d e f g h
# 5
# Output
# ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']

cards = input().split(" ")
shuffles = int(input())

for i in range(shuffles):
    first_half = []
    second_half = []
    new_cards = []
    for j in range(0, len(cards) // 2):
        first_half.append(cards[j])
    for k in range(len(cards) // 2, len(cards)):
        second_half.append(cards[k])
    for m in range(len(first_half)):
        new_cards.append(first_half[m])
        new_cards.append(second_half[m])
    cards = new_cards
print(cards)
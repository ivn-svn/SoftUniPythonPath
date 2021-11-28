# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from
# 1 to 11. Any player may be sent off the field by being given a red card. If one of the teams has less than
# 7 players remaining, the game is stopped immediately by the referee, and the team with less than 7 players loses.
#
# A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number. e.g. the card
# 'B-7' means player #7 from team B received a card. (index 6 of the list)
# The task: Given a list of cards (could be empty),
# return the number of remaining players on each team at the end of the
# game in the format: "Team A - {players_count}; Team B - {players_count}". If the game was terminated print an
# additional line: "Game was terminated"
# Note for the random tests: If a player that has already been sent off receives another card - ignore it.
# Input
# The input (the cards) will come on a single line separated by a single space
# Output
# Print the remaining players as described above and add another line (as shown above) if the game was terminated
card_input = input().split(' ')
#
idx = 0
#
card = ''
player = 0
cards_list = []
players_teama = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
players_teamb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
terminated = False
#
players_counta = len(players_teama)
players_countb = len(players_teamb)
# terminated = False
# #
# while terminated != True:
for i in range(0, len(card_input)):
    cards_list.append(card_input[i].split("-"))
    c = cards_list[i]
    card = c[0]
    player = c[1]  # Проблемът е, че тук се получава списък в списъка.
    if card == "A":
        if int(player) not in players_teama:
            pass
        else:
            players_teama.remove(int(player))

    elif card == "B":
        if int(player) not in players_teamb:
            pass
        else:
            players_teamb.remove(int(player))
        #
    players_counta = len(players_teama)
    players_countb = len(players_teamb)
    if players_counta < 7 or players_countb < 7:
        terminated = True
        break
print(f"Team A - {players_counta}; Team B - {players_countb}")
if terminated:
    print("Game was terminated")
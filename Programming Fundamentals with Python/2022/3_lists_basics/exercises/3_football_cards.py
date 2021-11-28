team_a = 11
team_b = 11
game_stop = False
players = input()
players_list = players.split(' ')
players_listdash = []
while not game_stop:
    for z in players_list:
        players_listdash = players_list[players_list.index(z)].split('-')
        if players_listdash[0] == 'A' and team_a >= 7:
            team_a -= 1
        elif 'B' == players_listdash[0] and team_b >= 7:
            team_b -= 1
        else:
            break
    if team_a <= 7:
        game_stop = True
        print(f"Team A - {team_a}; Team B - {team_b}")
        print("Game was terminated")
        break
    elif team_b <= 7:
        game_stop = True
        print(f"Team A - {team_a}; Team B - {team_b}")
        print("Game was terminated")
        break
    else:
        print(f"Team A - {team_a}; Team B - {team_b}")
        break
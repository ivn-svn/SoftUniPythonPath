# На круизния кораб, на който Ани прекарвала почивката си,
# се организирали т. нар. круизни игри. Всеки участник избирал в колко игри да участва, като всяко състезание му
# носело даден брой точки. Възможните игри били волейбол, тенис и бадминтон, като в зависимост от трудността на
# играта получените точки се увеличавали както следва: волейболът увеличавал точките със 7%, тенисът с 5%,
# а бадминтонът с 2%. Играчът печели ако средноаритметичният
# брой точки от всеки един вид игра е поне 75, в противен случай губи.
# Напишете програма, която пресмята дали играчът е победил или загубил и изчислява общият му брой точки.
win = False
#
average_points = 0
volleyball = 0
tennis = 0
badminton = 0
#
player_name = str(input())
games_played = int(input())
game_type = str(input())
points_num = int(input())
# Колко пъти е играл всяка игра?
count_times_played = 0
volleyball_points = 0
volleyball_games_counter = 0
for game in range(games_played):
    game_type = input()
    current_points = int(input())
    if game_type == 'volleyball':
        # curr_p += curr_p * 0.07
        # curr_p += curr_p + curr_p * 0.07
        current_points = current_points * 1.07

    elif game_type == 'tennis':

    if volleyball_average >= 75 and tennis_average >= 75:
        print(f"Congratulations, {player_name} You won the cruise games with {points_num} points.")
    else:
        print(f"Sorry, {player_name}, you lost. Your points are only {points_num}.")
initial_pts_num = int(input())
# 1. Read start points
start_points = int(input())
points = start_points
moves_counter = 0
# 2. Until start points > 0
while points > 0:
# 2.1. Read move type
    move_type = input()
# 2.2. Count moves
moves_counter += 1
# 2.2. Check if in bullseye
# 2.2. Read points
# 2.3. Calculate points (x2, x3 )
# 2.4. Calculate points ()
current_points = int(input())
# 2.5. Count moves
if move_type == 'double ring':
    current_points *= 2
# 2.6. Subtract from points
points -= current_points
# 2.7. Check if  points < 0
if points < 0:
# 3. Print
# 3.1. Won
# 3.2. Won bullseye

# На конзолата се отпечатва един ред:
#     • Ако играчът спечели чрез достигане на нула точки:
# 	"Congratulations! You won the game in {брой ходове} moves!"
#     • Ако играчът спечели чрез уцелване на центъра на мишената:
# 	"Congratulations! You won the game with a bullseye in {брой ходове} moves!"
#     • Ако играчът загуби:
# 	"Sorry, you lost. Score difference: {брой отрицателни точки}."
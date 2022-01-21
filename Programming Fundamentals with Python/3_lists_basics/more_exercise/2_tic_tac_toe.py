# # https://judge.softuni.bg/Contests/Practice/Index/1726#1
# You will receive a field of a tic-tac-toe game in three lines containing numbers separated by a single space.
# Legend:
# 0 - empty space
# 1 - first player move
# 2 - second player move
# Find out who the winner is. If the first player wins print "First player won", otherwise
# if the second player wins print "Second player won", otherwise print "Draw!"
tic_tac0 = input().split(' ')
tic_tac1 = input().split(' ')
tic_tac2 = input().split(' ')
tic_result0 = 0
tic_result1 = 0
tic_result2 = 0
#
for x in tic_tac0:
    tic_result0 += int(x)
for z in tic_tac1:
    tic_result1 += int(z)
for y in tic_tac2:
    tic_result2 += int(y)
if tic_result0 > tic_result1 and tic_result2:
    print('First player won')
elif tic_result1 < tic_result2 and tic_result0:
    print('Second player won')
elif tic_result2 < tic_result1 and tic_result0:
    print('Third player won')
elif tic_result0 == tic_result1 == tic_result2:
    print("Draw!")

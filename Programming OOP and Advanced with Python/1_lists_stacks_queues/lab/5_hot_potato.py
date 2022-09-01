# 5.	Hot Potato
# Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid. 
# Every nth toss, the child holding the potato leaves the game. When a kid leaves the game, it passes the potato to the next kid. 
# It continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato. On the first line, you will receive kids' names, separated by a single space. 
# On the second line, you will receive the nth toss (integer) in which a child leaves the game.
# Print every kid who is removed from the circle in the format "Removed {kid}". In the end, print the only kid left in the format "Last is {kid}".
# Examples
# Input	Output
# Tracy Emily Daniel
# 2	Removed Emily
# Removed Tracy
# Last is Daniel

from collections import deque

#kids_string = input()
kids_string = 'George Peter Michael William Thomas'
# tosses = '10'
tosses = input()

kids = deque(kids_string.split(' '))
tosses_int = int(tosses)

current_count = 0

while len(kids) > 1:
    current_count += 1
    kid = kids.popleft()
    if current_count < tosses_int:
        kids.append(kid)
    else:
        print(f'Removed {kid}')
        current_count = 0

print('Last is ' + kids[0])
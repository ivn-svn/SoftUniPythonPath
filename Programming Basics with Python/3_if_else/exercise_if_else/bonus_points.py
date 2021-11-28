starting_points = int(input())

bonus = 0
if starting_points % 2 == 0:
    bonus += 1
else:
    if starting_points % 10 == 5:
        bonus += 2
if starting_points <= 100:
    bonus += 5
    print(bonus)
    print(starting_points + bonus)
elif 100 < starting_points < 1000:
    bonus = starting_points * 0.2 + bonus
    print(bonus)
    print(starting_points + bonus)
elif starting_points > 1000:
    bonus = starting_points * 0.1 + bonus
    print(bonus)
    print(starting_points + bonus)
#
excess_food = 0
excess_hay = 0
excess_cover = 0
#
food = float(input())
hay = float(input())
cover = float(input())
guinea_pig_weight = float(input())
#

for i in range(0, 30):
    if i % 2 == 0:
        food -= 300
        food *= 0.05
    elif i % 3 == 0:
        food = food + (food / 3)
    else:
        food -= 300


print(f"Everything is fine! Puppy is happy! Food: {excess_food}, Hay: {excess_hay}, Cover: {excess_cover}.")

print("Merry must go to the pet store!")
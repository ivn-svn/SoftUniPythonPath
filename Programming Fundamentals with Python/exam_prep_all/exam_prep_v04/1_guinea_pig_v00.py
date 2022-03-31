def enough_check(enough):
    if enough:
        print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {covers:.2f}.")
    else:
        print("Merry must go to the pet store!")


food = float(input())
hay = float(input())
cover = float(input())
guinea_pig_weight = float(input())
put_cover = (guinea_pig_weight / 3)
enough = None
###
##
#
hay_list = []
# food_list = [y for y in range(1, 31) if y % 2 == 0]
cover_list = [x for x in range(1, 31) if x % 3 == 0]
# hays_list = list(map(lambda a: a * a, cover_list1))
hays_list = []
covers = cover - (len(cover_list) * put_cover)


food_suff = food - (30 * 0.3)

if food_suff > 0 and covers > 0:
    enough = True
    for day in range(1, 31):
        food -= 0.3
        if day % 2 == 0:
            hay -= (food * 0.05)
            if hay <= 0:
                hay += (food * 0.05)
                enough = False
                break
        elif day % 3 == 0:
            cover -= put_cover
else:
    enough = False

enough_check(enough)
# print(enough)

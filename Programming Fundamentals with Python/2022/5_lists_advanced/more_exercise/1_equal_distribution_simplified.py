# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what,
# and that is exactly what you are called to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", "). On the second line,
# you will be given the minimum wealth. You should distribute the wealth so that no part of the population has less than
# the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible"
# 2, 3, 5, 15, 75
# 5

wealthlist = str(input())
min_wealth = int(input())
ints_wealthlist = [int(z) for z in wealthlist.split(', ')]
to_distribute = 0
abundance = 0
diff = 0
socialism_built = False
redis_list = []


def wealth_redistribution(a, t, s, re, dif):
    while s == False:
        for wealth in range(0, len(ints_wealthlist)):
            wealthiest = max(ints_wealthlist)
            poorest = min(ints_wealthlist)
            if ints_wealthlist[wealth] > min_wealth:
                a += (ints_wealthlist[wealth] - min_wealth)
                listofwealthypeople = []
                listofwealthypeople.append(wealth)
            if ints_wealthlist[wealth] < min_wealth:
                t += (min_wealth - ints_wealthlist[wealth])
                listofpoorpeople = []
                listofpoorpeople.append(wealth)
        if a < t:
            s = False
            print("No equal distribution possible")
            break
        elif a >= t:
            for currentwealth in ints_wealthlist:
                while currentwealth < min_wealth:
                    a -= 1
                    currentwealth += 1
                else:
                    if currentwealth > min_wealth:
                        dif = currentwealth - t
                        if currentwealth == wealthiest:
                            currentwealth = dif
                #
                redis_list.append(currentwealth)
            re = [r for r in redis_list]
        s = True

    return re


# if wealth_redistribution(abundance, to_distribute, socialism_built, redis_list, diff) == None:
#     pass
# else:

to_print = wealth_redistribution(abundance, to_distribute,
                                  socialism_built, redis_list, diff)
# print(wealth_redistribution(abundance, to_distribute, socialism_built, redis_list, diff))

print(to_print)

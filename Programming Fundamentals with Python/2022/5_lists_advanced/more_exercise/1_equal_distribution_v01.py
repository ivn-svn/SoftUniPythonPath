# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what,
# and that is exactly what you are called to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", "). On the second line,
# you will be given the minimum wealth. You should distribute the wealth so that no part of the population has less than
# the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible"
# 2, 3, 5, 15, 75
# 5
wealthlist = str(input())
minwealth = int(input())
ints_wealthlist = [int(z) for z in wealthlist.split(', ')]
# Variables to calculate abundance and wealth to be distributed
todistribute = 0
abundance = 0
#
diff = 0
#
socialismbuilt = False

# Function to calculate what is to be distributed and what is in abundance:
redistributionlist = []


def wealthRedistribution(a, t, s, re, dif):
    while s != True:
        for wealth in range(0, len(ints_wealthlist)):  # This is a for cycle of the KGB to learn about the wealth
            # of the population.
            # If the person is rich, the commies have to identify it and reduce the income:
            wealthiest = max(ints_wealthlist)
            poorest = min(ints_wealthlist)
            if ints_wealthlist[wealth] > minwealth:
                a += (ints_wealthlist[wealth] - minwealth)
                listofwealthypeople = [] # Indexing wealthy people; the list shall contain the index on which
                # the person can be found within the ints_wealthlist
                listofwealthypeople.append(wealth)
            if ints_wealthlist[wealth] < minwealth:
                t += (minwealth - ints_wealthlist[wealth])
                # Indexing poor people; the list shall content the index on which
                # the person can be found within the ints_wealthlist
                listofpoorpeople = []
                listofpoorpeople.append(wealth)
        if a < t:  # If there is not enough wealth to redistribute / if the abundance is less than the wealth to be
            # redistributed:
            s = False
            print("No equal distribution possible")
            break
        elif a >= t:
            # If the abundance is more than the wealth to be redistributed, then there surely will be enough wealth
            # for everyone, hence a new redistribution for cycle will start:
            for currentwealth in ints_wealthlist:
                while currentwealth < minwealth:
                    a -= 1
                    currentwealth += 1
                else:
                    if currentwealth > minwealth:
                        dif = currentwealth - t
                        redistributionlist.append(dif)
                        ints_wealthlist.pop(ints_wealthlist.index(currentwealth))

                redistributionlist.append(currentwealth)
            s = True
            re = [r for r in redistributionlist]
            return re
if wealthRedistribution(abundance, todistribute, socialismbuilt, redistributionlist, diff) == None:
    pass
else:
   print(wealthRedistribution(abundance, todistribute, socialismbuilt, redistributionlist, diff))

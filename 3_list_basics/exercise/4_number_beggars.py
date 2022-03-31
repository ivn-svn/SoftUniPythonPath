# Your task here is pretty simple: given a list of numbers and an amount of beggars, you are supposed to return a list
# with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.
# For example: [1,2,3,4,5] for 2 beggars will return a result of 9 and 6, as the first one takes [1,3,5], the second
# collects [2,4].
# The same list with 3 beggars would have in turn have produced a better outcome for the second beggar: 5, 7 and 3, as
# they will respectively take [1, 4], [2, 5] and [3].
# Also note that not all beggars have to take the same amount of "offers", meaning that the length of the list
# is not necessarily a multiple of n; length can be even shorter, in which case the last beggars
# will of course take nothing (0).
# Input
# You will receive 2 lines of input: a single string containing the numbers separated by a comma and a space ", ".
# On the second line you will receive the number of beggars
# Output
# Print a list of all the sums that each beggar made
import math
money_collected = input().split(", ")
number_beggars = int(input())
loot = []
idx = 0
itter = math.ceil(len(money_collected) / number_beggars)
for beggar in range(idx, number_beggars):
    try:
        loot.append(int(money_collected[beggar]))
        idx += 1
    except IndexError:
        continue
if itter > 1:
    while math.ceil(idx / number_beggars < itter):
        try:
            for b in range(0, number_beggars):
                loot[b] += int(money_collected[idx])
                idx += 1

        except IndexError:
            break
if number_beggars > len(money_collected):
    loot.append(0)
print(loot)
# test input: 5, 5, 6, 7, 15
# minwealth: 6

wealthlist = input()
minwealth = int(input())
wealthlistints = [int(x) for x in wealthlist.split(", ")]
for i in range(len(wealthlistints)):
    wealthiest = max(wealthlistints)
    robtherich = wealthlistints.index(wealthiest)
    poorest = min(wealthlistints)
    if wealthlistints[i - 1] < minwealth:
        dif = minwealth - poorest
        while wealthlistints[i - 1] < minwealth:
            wealthlistints[robtherich] -= dif
            wealthlistints[i - 1] += dif
    else:
        pass
if min(wealthlistints) < minwealth:
    print("No equal distribution possible")
else:
    print(wealthlistints)
wealthlist = input()
minwealth = int(input())
wealthlistints = [int(x) for x in wealthlist.split(", ")]
for i in range(len(wealthlistints)):
    wealthiest = max(wealthlistints)
    robtherich = wealthlistints.index(wealthiest)
    poorest = min(wealthlistints)
    while wealthlistints[i - 1] < minwealth:
        wealthlistints[robtherich] -= 1
        wealthlistints[i - 1] += 1
if min(wealthlistints) < minwealth:
    print("No equal distribution possible")
else:
    print(wealthlistints) 
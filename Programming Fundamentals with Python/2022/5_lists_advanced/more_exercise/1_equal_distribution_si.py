# test input: 5, 5, 6, 7, 15
# minwealth: 6

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
wealthlistints = sorted(wealthlistints)
print(wealthlistints)
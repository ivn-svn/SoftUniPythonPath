# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list. You should remove the smallest ones, and then,
# you should print all the numbers that are left in the list, separated by a comma and a space ", ".
# Input
# 10 9 8 7 6 5
# 3
# Output
# 10, 9, 8
userinput = input().split(' ')
numcount = int(input())
#
finallist = []
toremove = sorted([int(x) for x in userinput])
# print(toremove)
for i in range(0, numcount):
    toremove.remove(toremove[0])
toremove = [str(u) for u in toremove]

for k in userinput:
    if str(k) in toremove:
        finallist.append(k)
print(', '.join(finallist))

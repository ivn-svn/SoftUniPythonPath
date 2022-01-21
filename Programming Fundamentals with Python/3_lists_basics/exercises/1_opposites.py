# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.
n = input()
splited = n.split(' ')
newlist = []
for x in splited:
    turnopposite = int(x) * -1
    neturnop = str(turnopposite)
    newlist.append(neturnop)
    ' '.join(newlist)
    newlist1 = [int(x) for x in newlist]
print(newlist1)


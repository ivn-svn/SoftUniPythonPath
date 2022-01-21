userinput = [int(x) for x in input().split(' ')]


def evenFilter(z):

    if z % 2 == 0:
        return True
    else:
        return False


userinput = filter(evenFilter, userinput)
outputeven = []
for i in userinput:
    outputeven.append(i)
print(outputeven)

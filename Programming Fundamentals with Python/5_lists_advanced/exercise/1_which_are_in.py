# Given two lists of strings print a new list of the strings that contains words from the first
# list which are substrings of any of the strings in the second list (only unique values)
datalist = input().split(", ")
datalist1 = input().split(", ")
for x in datalist:
    checkstr = list(x)
    for y in range(0, len(checkstr)):
        if checkstr[y] in datalist[x]

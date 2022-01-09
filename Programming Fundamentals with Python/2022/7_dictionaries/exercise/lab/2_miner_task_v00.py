# You will be given a sequence of strings, each on a new line. Every odd line on the console represents a resource
# (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is to collect the resources
# and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].
# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop
# Gold -> 155
# Silver -> 10
# Copper -> 17
res_gathered = {}
strseq = ''
ln = 0
reslist = []
toadd = False
while strseq.lower() != 'stop':
    strseq = input()
    if strseq.isnumeric() == False and strseq not in reslist:
        reslist.append(strseq)
        ln += 1
        res_gathered[strseq] = 0
        toadd = False
    elif strseq.isalpha() == True and strseq in reslist:
        toadd = True
        pass
    elif toadd == True and strseq.isnumeric() == True:
        res_gathered[ln - 1] += int(strseq)
        toadd = False

else:
    print(res_gathered)
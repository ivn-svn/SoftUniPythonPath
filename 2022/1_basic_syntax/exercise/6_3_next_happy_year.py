current_year = int(input())
nextyr = current_year + 1
yrlist = yrcount = list(str(nextyr))
for x in yrlist:
    yrcount = list(str(nextyr)).count(x)
    while yrcount != 1:
        nextyr += 1
        yrcount = list(str(nextyr)).count(x)
    else:
        nextyr = str(yrlist)
        print(nextyr)
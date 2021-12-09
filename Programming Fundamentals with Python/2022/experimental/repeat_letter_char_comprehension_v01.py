# Task:
# The input given to the console would for example be:
# aaabbcccccdee
# The code should output the repeating characters with an digit index
# for how many encounters of the given char there were in the input, for example the
# above input should result in the following:
# 3a2b5c1d2e
user_input = input()
lstusrinp = list(user_input)
newlist = []
thirdlist = [newlist.append(x) for x in lstusrinp if x not in newlist]
fourthlist = [str(lstusrinp.count(y)) + y for y in newlist]
print(''.join(fourthlist))
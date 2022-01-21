letters = "asdfHRbySFss"


def iscap(x): return x.isupper()


print(filter(iscap, letters))
# letters = input()
# uppers = [l for l in letters if l.isupper()]
# print(uppers)

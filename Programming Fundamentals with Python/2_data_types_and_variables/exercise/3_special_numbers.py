n = int(input())
special_digits = [5, 7, 11]
number = 0
sum_of = 0
dict_n = []
boolspec = False
for x in range(1, n + 1):
    dict_n = list(str(x))
    if x > 10:
        sum_of = int(dict_n[0]) + int(dict_n[1])
        if sum_of in special_digits:
            boolspec = True
        else:
            boolspec = False
    elif x == 5 or x == 7 or x == 11:
        boolspec = True
    else:
        boolspec = False

    if boolspec == True:
        print(f'{x} -> True')
    elif boolspec == False:
        print(f'{x} -> False')

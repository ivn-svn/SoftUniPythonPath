# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
#     • even
#     • odd
#     • negative
#     • positive

listeven = []
listodd = []
listnegative = []
listpositive = []
isnum = ''
n = int(input())
for x in range(1, n + 1):
    ints = int(input())
    if ints % 2 == 0:
        listeven.append(ints)
    if ints % 2 == 1:
        listodd.append(ints)
    if ints >= 0:
        listpositive.append(ints)
    if ints < 0:
        listnegative.append(ints)
isnum = input()
if isnum == 'even':
    print(listeven)
elif isnum == 'odd':
    print(listodd)
elif isnum == 'negative':
    print(listnegative)
elif isnum == 'positive':
    print(listpositive)

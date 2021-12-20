# Result should be:
# 30% [%%%.......]
# Still loading...
# 50% [%%%%%.....]
# Still loading...
# 100% Complete!
# [%%%%%%%%%%]
num = int(input())
checkdiv = num % 10
barprogress = num // 10
barprogresspercent = barprogress * 10
message = ''
dots = ''

def load_bar(b, m, d):
    baritself = ''
    for i in range(0, b):
        baritself += '%'

    if b < 10:
        m = 'Still loading...'
        d = '.' * (10 - b)
        return f"{str(barprogresspercent)}% [{baritself}{d}]\n{m}"
    elif b == 10:
        m = 'Complete!'
        d = '.' * (10 - b)
        return f"{str(barprogresspercent)}% {m}\n[{baritself}]"
#
if 0 < num <= 100 and checkdiv == 0:
    print(load_bar(barprogress, message, dots))


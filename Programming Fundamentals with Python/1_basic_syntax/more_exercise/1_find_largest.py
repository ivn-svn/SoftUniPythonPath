_input = input()
y = [int(x) for x in _input]
z = sorted(y, reverse=True)
p = ''
for m in z:
    p += str(m)
print(p)
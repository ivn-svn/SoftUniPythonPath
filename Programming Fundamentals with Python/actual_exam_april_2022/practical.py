a = 5
b = a > 2
if not a:
    print(a)
if b:
    print(b)

print(bool(-1))
print(bool(""))
print(bool(0))
print(bool(None))

a = [1, 2, 3, 4, 5]
a.pop(2)
print(a)
a = [1, 2, 3, 4, 5]

del a[2]
print(a)
a = [1, 2, 3, 4, 5]

a.remove(3)
print(a)
a = [1, 2, 3, 4, 5]

for i in range(10, 3, -2):
    print(i, end=" ")

name = "George"
name[2] = "m"
print(name[2])
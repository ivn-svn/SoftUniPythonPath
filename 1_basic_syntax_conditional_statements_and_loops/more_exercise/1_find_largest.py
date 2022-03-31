# https://judge.softuni.bg/Contests/1720
# Given a number, print the largest number that can be formed from the digits of the number given.
_input = input()
y = [int(x) for x in _input]
z = sorted(y, reverse=True)
p = ''
for m in z:
    p += str(m)
print(p)
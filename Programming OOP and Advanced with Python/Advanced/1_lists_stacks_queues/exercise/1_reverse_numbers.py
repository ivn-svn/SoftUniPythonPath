#
# Input	Output
# 1 2 3 4 5	5 4 3 2 1
#
# Write a program that reads a string with N integers from the console, 
# separated by a single space, and reverses them using a stack. Print the reversed 
# integers on one line, separated by a single space.
#
#n = input()
#
from collections import deque
#
n = '1 2 3 4 5'
#
n_splt = deque(n.split(' '))
new = []
new_str = ''
while n_splt:
    old = n_splt.pop()
    new.append(old)

new_str = ' '.join(new)
print(new_str)
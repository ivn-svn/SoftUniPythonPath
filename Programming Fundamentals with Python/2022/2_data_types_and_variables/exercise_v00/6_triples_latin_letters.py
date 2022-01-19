# Write a program to read an integer N and print 
# all triples of the first N small Latin letters, ordered alphabetically:
num = int(input())
for first in range(0, num):
    for second in range(0, num):
        for third in range(0, num):
            print(f"{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}")

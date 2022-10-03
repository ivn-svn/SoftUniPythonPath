# Write a program that reads from the console a sequence of N usernames and keeps a collection only 
# of the unique ones. On the first line, you will receive an integer N. On the next N lines,
#  you will receive a username. Print the collection on the console (the order does not matter):
#
usernames = set()
n = int(input())
for line in range(0, n):
    usernames.add(input())

for name in usernames:
    print(name, end='\n')

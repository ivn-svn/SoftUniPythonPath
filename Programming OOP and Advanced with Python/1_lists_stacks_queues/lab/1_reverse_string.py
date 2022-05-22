# https://judge.softuni.org/Contests/Practice/Index/1830#0

thestack = list(input())
[print(thestack.pop(), end="") for idx in range(len(thestack))]
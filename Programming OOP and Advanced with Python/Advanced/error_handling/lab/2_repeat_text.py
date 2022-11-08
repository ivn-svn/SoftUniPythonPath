
try:
    repeatable, times = input(), int(input())
    print(repeatable * times)
except ValueError:
    print("Please, enter an integer")
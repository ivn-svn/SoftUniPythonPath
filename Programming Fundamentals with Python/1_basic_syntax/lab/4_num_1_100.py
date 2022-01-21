number = float(input())
while number < 1 or number > 100:
    number = float(input())
print(f"The number {number:.9g} is between 1 and 100")
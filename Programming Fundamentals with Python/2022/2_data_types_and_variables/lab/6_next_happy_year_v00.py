happy_year = int(input()) + 1

while len(set(str(happy_year))) != len(str(happy_year)):
    happy_year += 1

print(happy_year)
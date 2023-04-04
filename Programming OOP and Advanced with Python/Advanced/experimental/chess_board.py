
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

for row in range(8, 0, -1):
    for letter in letters:
        print(f" {letter}{row} ", end="") 
    print("\n")

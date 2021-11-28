starting_number = int(input())
final_number = int(input())
magic_number = int(input())

combinations = 0
is_found = False

for i in range(1, starting_number + 1):
    for j in range(1, final_number + 1):
        combinations += 1

        if i + j == magic_number:
            is_found = True
            break
        else:
            is_found = False
if is_found == True:
    print(f"Combination N:{combinations} ({i} + {j} = {magic_number})")
elif is_found == False:
    print(f"{combinations} combinations - neither equals {magic_number}")

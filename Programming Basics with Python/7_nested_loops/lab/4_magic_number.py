firstn = int(input())
secondn = int(input())
magicn = int(input())
combo_counter = 0
check_if_in_magic = False
is_it_over = False
for firstn in range(1, firstn + 1):
    for secondn in range(1, secondn + 1):
        sum_firstn_secondn = firstn + secondn
        combo_counter += 1
        if magicn == sum_firstn_secondn:
            check_if_in_magic = True
            break
        elif combo_counter >= secondn:
            is_it_over = True
if check_if_in_magic is True:
    print(f"Combination N: {combo_counter}")
elif is_it_over is True:
    print(f"{combo_counter} combinations - neither equals {magicn}")
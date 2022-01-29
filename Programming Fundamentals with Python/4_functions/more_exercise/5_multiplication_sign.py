# Given 3 ints... Write a program that finds if their result is negative, positive, or zero.
# Try w\o multiplying the 3 numbers.
int1, int2, int3 = int(input()), int(input()), int(input())
list_ = [int1, int2, int3]
list_pos = []
list_neg = []


def is_negative(list_):
    for num in list_:
        if num < 0:
            list_neg.append(num)
        elif num >= 1:
            list_pos.append(num)
    if 0 in list_:
        return 'zero'
    else:
        if len(list_neg) == 1:
            return 'negative'
        elif len(list_neg) == 2:
            return 'positive'
        elif len(list_neg) == 3:
            return 'negative'
        else:
            return 'positive'
print(is_negative(list_))

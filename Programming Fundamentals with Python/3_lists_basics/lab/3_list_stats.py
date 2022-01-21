n = int(input())
count_positives = []
sum_negatives = []
for i in range(n):
    number = int(input())
    if number >= 0:
        count_positives.append(number)
    else:
        sum_negatives.append(number)
print(f"Count of positives: {len(count_positives)}. Sum of negatives: {sum_negatives}")
#      List Statistics
# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
#     • One with all the positives (including 0) numbers
#     • One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
#  Sum of negatives: {sum_of_negatives}"
count_positives = 0
sum_of_negatives = 0
negatives = []
positives = []
#
n = int(input())
#
for x in range(1, n + 1):
    y = int(input())
    if y > 0:
        positives.append(y)
    elif y < 0:
        negatives.append(y)
count_positives = len(positives)
sum_of_negatives = sum(negatives)
print(f"{positives}")
print(f"{negatives}")
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
import sys
sum_num = 0
max_num = -sys.maxsize
diff = 0
n = int(input())
for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_num += num
sum_num -= max_num
if sum_num == max_num:
    print("Yes")
    print(f"Sum = {sum_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - sum_num)}")
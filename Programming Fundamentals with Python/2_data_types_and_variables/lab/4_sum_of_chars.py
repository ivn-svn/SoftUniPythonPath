n = int(input())
ord_str = ''
sum_of_ord = 0
for x in range(1, n + 1):
    ord_str = str(input())
    sum_of_ord += ord(ord_str)
print(f"The sum equals: {sum_of_ord}")
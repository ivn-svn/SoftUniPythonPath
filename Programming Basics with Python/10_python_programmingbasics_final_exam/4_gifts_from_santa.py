# n = int(input())
# #
# p1 = 0
# p2 = 0
# p3 = 0
# #
# for i in range(1, n + 1):
#     number = int(input())
# #
#     if number % 2 == 0:
#         p1 += 1
#     if number % 3 == 0:
#         p2 += 1
#     if number % 4 == 0:
#         p3 += 1
# #
# percentage1 = p1 / n * 100
# percentage2 = p2 / n * 100
# percentage3 = p3 / n * 100
# print(f"{percentage1:.2f}%")
# print(f"{percentage2:.2f}%")
# print(f"{percentage3:.2f}%")

#

n=int(input())
m=int(input())
s=int(input())

for i in range(m,n,-1):
    if i%3==0 and i%2==0:
        if i!=s:
            print(i, end=' ')
        elif i==s:
            break
num = int(input())
i = 0
k = 0
j = 0
def ikjfunc():
    print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")
for i in range(0, num):
    for k in range(0, num):
        for j in range(0, num):
            ikjfunc()
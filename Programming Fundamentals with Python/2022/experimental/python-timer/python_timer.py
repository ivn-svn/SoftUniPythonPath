import time 

user_start = int(input())
counter = 0
tic = time.perf_counter()

user_end = int(input())

while True:
    toc = time.perf_counter()
    if toc - tic > 1:
        counter -= 1
        print(counter)
        if counter <= 0:
            print("Bang!")
            break
        tic = toc


# print(time.perf_counter)
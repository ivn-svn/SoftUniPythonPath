def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg


nlist = input().split(" ")
toaverage = [int(y) for y in nlist]

average = cal_average(toaverage)

nums_to_use = [int(z) for z in nlist if int(z) > average]
nums_to_use.sort(reverse=True)
# print(f"nums all : {nums_to_use}")
nums_last_list = []
counter = 0
for n in nums_to_use:
    if counter < 5:
        nums_last_list.append(int(n))
        counter += 1
#
# print(nums_last_list)
# print(nums_last_list)
# nums_last_list.sort(key=lambda x: (int(x)))

nums_last_list = [str(k) for k in nums_last_list]
final_list = " ".join(nums_last_list)
if len(final_list) == 0:
    print("No")
else:
    print(final_list)

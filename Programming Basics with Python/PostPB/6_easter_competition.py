# Link to Judge: https://judge.softuni.bg/Contests/Practice/Index/1637#10
#from operator import itemgetter
baker_name = ''
review_mark = 0
#
baker_pts = 0
#
bakers_list = []
num_cosunak = int(input())
for x in range(1, num_cosunak + 1):
    baker_name = str(input())
    review_mark = input()
    baker_pts += int(review_mark)
    while review_mark != 'Stop':
        review_mark = input()
        if review_mark == 'Stop':
            break
        else:
            review_mark = int(review_mark)
            baker_pts += review_mark
    bakers_list.append([baker_name, baker_pts])
    baker_pts = 0
def Sort_Tuple(bakers_list):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    bakers_list.sort(reverse=True, key=lambda x: x[1])
    return bakers_list
Sort_Tuple(bakers_list)
#r = map(itemgetter(1), bakers_list)
names = [item[0] for item in bakers_list]
nums = [item[1] for item in bakers_list]
print(f'{names[0]} has {nums[0]} points.')
print(f'Is the new number 1!')
#
#
print(f'{names[0]} won the competition with {nums[0]} points.')
# while 1 <= review_mark <= 10:


# #
# print(f'{baker_name} is the new number 1!')
# #
# print(f'"{baker_name} won competition with {baker_pts} points!"')

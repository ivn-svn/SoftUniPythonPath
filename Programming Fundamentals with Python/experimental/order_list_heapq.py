# This strictly follows your requirements not to use sort(), min(), max() but also uses Python best practice by not re-inventing the wheel.

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
import heapq
heapq.heapify(data_list)
new_list = []
while data_list:
    new_list.append(heapq.heappop(data_list))
print(new_list)
# I suggest having a look in the Python library for heapq.py to see how it works. Heapsort is quite a fun sorting algorithm as it lets you 'sort' an infinite stream, i.e. you can quickly get at the currently smallest item but also efficiently add new items to the the data to be sorted.
#
# # Share
# # Improve this answer
# # Follow
# # answered Aug 15 '12 at 8
# Source: https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function
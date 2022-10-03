# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
# Write a program that finds the longest intersection. 
# You will be given a number N. On each of the next N lines you will be
# given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}".
# You should find the intersection of these two ranges. The start and end numbers 
# in the ranges are inclusive. 
# Finally, you should find the longest intersection of all N intersections,
# print the numbers that are included and its length in the format: 
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
n = int(input())
list_intersections = list()
for i in range(0, n):
    user_input = input()
    range1 = user_input.split("-")[0]
    range1_ints = [z for z in range(int(range1.split(",")[0]), int(range1.split(",")[1])) + 1]
    range2 = user_input.split("-")[1]
    range2_ints = [y for y in range(int(range2.split(",")[0]), int(range2.split(",")[1])) + 1]
    intersection = set()
    for num in range1_ints:
        if num in range2_ints:
            intersection.add(num)
    list_intersections.append(intersection)

    intersection = set()


#define the function#
def find_max_list(list):
    list_len = [len(i) for i in list]
    for item in list:
        if len(item) == max(list_len):
            return item

#print output#
longest_intersection_numbers = find_max_list(list_intersections)

length_longest_intersection = len(longest_intersection_numbers)



print(f"Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}")

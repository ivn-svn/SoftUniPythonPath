# Write a program to read a sequence of integers and find 
# and print the top 5 numbers greater than the average value in
#  the sequence, sorted in descending order.

# Input
# Read from the console a single line holding space-separated integers.
# Output
# Print the above-described numbers on a single line, space-separated. 
# If less than 5 numbers hold the property mentioned above, print less than 5 numbers. 
# Print "No" if no numbers hold the above property.
# Constraints
# All input numbers are integers in the range [-1 000 000 … 1 000 000]. 
# The count of numbers is in the range [1…10 000].
list_fit = list()
user_input = input().split(' ')
#
num_sum = 0
for num in user_input:
    num_sum += int(num)

average = num_sum // len(user_input)
for x in user_input:
    if int(x) > average:
        list_fit.append(int(x))
list_fit = list_fit.sort(reverse=True)

# if len(list_fit) == 0:
#     print("No")
if len(list_fit) == 0:
    print("No")

else:
    print(f"{list_fit}")
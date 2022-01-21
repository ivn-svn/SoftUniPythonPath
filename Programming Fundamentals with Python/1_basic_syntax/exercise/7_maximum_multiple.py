# •	Maximum Multiple
# On the first line, you will be given a positive number, 
# which will serve as a divisor. On the second line, you will receive a
#  positive number that will be the boundary. You should find the largest integer N, that is:
# 	•	 divisible by the given divisor
# 	•	  less than or equal to the given bound
# 	•	 greater than 0
# Note: it is guaranteed that N is found.


div_num = int(input())
boundary_num = int(input())
found = 0
for num in range(div_num, boundary_num + 1):
    if num % div_num == 0 and num > 0 and num <= boundary_num:
        found = num
print(found)

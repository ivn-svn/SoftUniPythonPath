# Да се напише програма, която чете 2*n-на брой цели числа, подадени от потребителя, и проверява дали сумата на първите
# n числа (лява сума) е равна на сумата на вторите n числа (дясна сума). При равенство печата " Yes, sum = " + сумата;
# иначе печата " No, diff = " + разликата. Разликата се изчислява като положително число (по абсолютна стойност).
nums_list = int(input())
diff = 0
sum_of_one = 0
sum_of_two = 0
for i in range(nums_list):
    user_input_prompt_one = int(input())
    sum_of_one += user_input_prompt_one
for i in range(nums_list):
    user_input_prompt_two = int(input())
    sum_of_two += user_input_prompt_two
if sum_of_one == sum_of_two:
    print(f"Yes, sum = {sum_of_one}")
else:
    diff = abs(sum_of_one - sum_of_two)
    print(f"No, diff = {diff}")
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
#     • "We have a perfect number!" - if the number is perfect.
#     • "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.
#
# Hint
# Every perfect number is half the sum of all its positive divisors (including itself) => the sum of all positive
# divisors (all of which are divided without remainder) of
# 6 is 1 + 2 + 3 + 6 = 12. Half of 12 is 6 => 6 is perfect number.
#     • You could read more about the perfect number here: https://en.wikipedia.org/wiki/Perfect_number
divisors_list = []
num = int(input())
perfect = False
not_perfect = False
aliquot_sum = 0
#
def perfect_check(n):
    for i in range(1, n + 1):
        if num % i == 0 and i != num:
            divisors_list.append(i)
            #print(divisors_list)
    aliquot_sum = sum(divisors_list)
    if aliquot_sum == num:
        return f"We have a perfect number!"
        # print({[str(x) for x in divisors_list]}.join(' + '))
        # return f"= {aliquot_sum}"
    else:
        return f"It's not so perfect."
        # print({[str(x) for x in divisors_list]}.join(' + '))
        # return f"= {aliquot_sum}"
print(perfect_check(num))
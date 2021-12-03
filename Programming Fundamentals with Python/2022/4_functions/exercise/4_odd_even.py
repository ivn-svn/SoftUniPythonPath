# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in
# a given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.
inputed = input()
inputed_list = list(str(inputed))


def odd_sum_f(inp):
    inpoddint = 0
    for m in inp:
        if int(m) % 2 == 1:
            inpoddint += int(m)
    return sum(inpoddint)


def even_sum_f(inp1):
    inpevenint = 0
    for k in inp1:
        if int(k) % 2 == 0:
            inpevenint += int(k)
    return sum(inpevenint)

odd_sum = odd_sum_f(inputed_list)
even_sum = even_sum_f(inputed_list)


print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
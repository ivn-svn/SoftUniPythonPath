# Read four integer numbers. Add first to the second, divide (integer)
# the sum by the third number and multiply the result by the fourth number. Print the result.
first_int = int(input())
second_int = int(input())
third_int = int(input())
fourth_int = int(input())
calc = ((first_int + second_int) // third_int ) * fourth_int
print(calc)
# Python program to check if
# given number is prime or not

num = int(input())

# If given number is greater than 1
if num > 1:

    # Iterate from 2 to n / 2
    for i in range(2, int(num / 2) + 1):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print("False")
            break
    else:
        print("True")

else:
    print("False")

    # От математиката се знае, че делителите на числото а са в интервала [2, а/2].
# A DP based
# Python 3
# program to print
# first n Tribonacci
# numbers.
#  code initially contributed by Nikita Tiwari and modified by me to print out the list in a particular manner.

def printTrib(n):
    dp = [0] * n
    dp[0] = dp[1] = 0;
    dp[2] = 1;

    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];

    for i in range(2, n):
        print(dp[i], end=" ")

n = int(input()) + 2
printTrib(n)


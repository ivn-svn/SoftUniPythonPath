# Unpacking using asterisk(*):

# When the number of variables is less than the number of elements, we add the elements together as a list to the variable with an asterisk.

# Example:

1
2
3
4
x,y,*z = [10,20,30,40,50]
print(x)
print(y)
print(z)

# Output is:

10
20
[30, 40, 50]
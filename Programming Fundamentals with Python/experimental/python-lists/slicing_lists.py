# Source:
# https://stackoverflow.com/questions/9027862/what-does-listxy-do
# L[x::y] means a slice of L where the x is the index to start from and y is the step size. Here are some examples you can try in the interpreter
#
L=range(20)
print(L)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# If you want every 3rd element
#
L[::3]
# [0, 3, 6, 9, 12, 15, 18]
#  https://judge.softuni.org/Contests/Practice/Index/2474#1.

# You are given an array with integers. Write a program to modify the elements after receiving the following commands:
# "swap {index1} {index2}" takes two elements and swap their places.
# "multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index. 
# Save the product at the 1st index.
# "decrease" decreases all elements in the array with 1.

# Master Class



# user_input = input().split(' ')
# command = user_input[0]
initial_array = list(input())
current_list = initial_array
#
swap, multiply, decrease = 'swap', 'multiply', 'decrease'
end = False

output = ''

class Master:
    def __init__(self, index1, index2, current_list):
        self.index1 = index1
        self.index2 = index2
        self.current_list = current_list

class Swap(Master):
    def __init__(self):
        super().__init__()

    def swap_(self, index1, index2, current_list):
        swapped = current_list
        swapped[index1], swapped[index2] = swapped[index2], swapped[index1]
        current_list = swapped
        return current_list
    

class Multiply(Master):  
    def __init__(self):
        super().__init__()
    def multiply_():
        current_list[index1] = (current_list[index1] * current_list[index2])
        return current_list

class Decrease:
    def __init__(self, current_list):
        current_list
    def decrease_(self, current_list):
        decreased = [int(x) - 1 for x in current_list]
        current_list = decreased
        return current_list

while end == False:
    if command == 'end':
        end = True
        break
    else:
        user_input = input().split(' ')
        command = user_input[0]

    if command == swap:
        index1, index2 = int(user_input[1]), int(user_input[2])
        current_list = Swap.swap_(index1, index2, current_list)
    elif command == multiply:
        index1, index2 = int(user_input[1]), int(user_input[2])
        current_list = Multiply.multiply_(index1, index2, current_list)

    elif command == decrease:
        index1, index2 = int(user_input[1]), int(user_input[2])
        current_list = Decrease.decrease_(index1, index2, current_list)

output = [str(x) for x in current_list]
output = ', '.join(output)
print(output)

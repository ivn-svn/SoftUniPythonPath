from math import pi
from math import pow

type = input()
area = 0.0
#
if type == "square":
    side_a = float(input())
    area = side_a * side_a
    #
elif type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
#
elif type == "circle":
    radius = float(input())
    area = pi * pow(radius, 2)
    #
elif type == "triangle":
    side_a = float(input())
    height = float(input())
    area = (side_a * height) / 2
    #
print(f'{area:.3f}')

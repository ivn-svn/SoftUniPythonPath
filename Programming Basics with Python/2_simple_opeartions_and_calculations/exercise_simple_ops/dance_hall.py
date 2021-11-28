# Dance Hall задача 5; Прости пресмятания
from math import pow
length = float(input()) * 100
width = float(input()) * 100
hall_area = length * width
#
wardrobe_a = float(input()) * 100
#
bench = hall_area / 10
#
dancer = 40
dancer_space = float(7000)
#
wardrobe_area = wardrobe_a * wardrobe_a
#
free_area = hall_area - wardrobe_area - bench
#
dancers_count = int(free_area / (40 + 7000))
#
print(dancers_count)
#

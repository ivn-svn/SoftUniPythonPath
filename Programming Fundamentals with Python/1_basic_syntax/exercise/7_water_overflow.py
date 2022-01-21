# 7. Water Overflow
# You have a water tank with capacity of 255 liters. On the next n lines, you will receive liters of water,
# which you have to pour in your tank. If the capacity is not enough, print
# "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank
capacity = 255
num = int(input())
tanked = 0
for x in range(0, num):
    data_input = int(input())
    if tanked + data_input > capacity:
        print("Insufficient capacity!")
        tanked -= data_input
    tanked += data_input
print(f"\n{tanked}")
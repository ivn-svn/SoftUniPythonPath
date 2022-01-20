# 3. Car Race
# Write a program that announces the winner of a car race. 
# You will receive a sequence of numbers. Each number represents the time needed for the car 
# to pass through that step (the index). There will be two cars. The first one starts from the left side, 
# and the other one starts from the right side. The middle index of the sequence is the finish line. 
# Calculate the total time each racer needs to reach the finish line and print 
# the winner with his total time (the racer with less time). If you have a zero in the list, you should reduce 
# the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format 
# "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.

# Input
# 29 13 9 0 13 0 21 0 14 82 12

finish_list = input().split(' ')
winner_anounce = ''
winner = ''
idx = 0
car1 = finish_list
car2 = finish_list[::-1]
#
car1time = 0
car2time = 0

finish_line = len(finish_list) // 2
for i in range(0, (len(finish_list) -1) // 2):

    # if i == finish_line:


    if int(car1[i]) == 0:
        car1time *= 0.80
    car1time += int(car1[i])
    if int(car2[i]) == 0:
        car2time *= 0.80
    car2time += int(car2[i])

    if car1time < car2time:
        left_right = "left"
        total_time = car1time
    else:
        left_right = "right"
        total_time = car2time
print(f"The winner is {left_right} with total time: {total_time:.1f}")


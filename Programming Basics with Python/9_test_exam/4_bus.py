# Автобус кара по маршрут София - Бургас. При тръгването си в автобуса има определен брой пътници.
# На всяка спирка се качват и слизат определен брой пътници. Броят на спирките се въвежда от конзолата.
# Също така, на всеки нечетен брой спирки се качват по двама проверяващи и слизат на четните спирки.
# Напишете програма, която изчислява колко пътника ще има в автобуса когато стигне в Бургас.
#
num_passengers = int(input())
stops = int(input())
final_num_passengers = 0
get_off_passengers = 0
get_in_passengers = 0
# Check if odd or even
# if_odd = False
# if_even = False
#
stops_counter = 0
for x in range(1, stops + 1):
    get_off_passengers_cycle = int(input())
    get_off_passengers += get_off_passengers_cycle
    get_in_passengers_cycle = int(input())
    get_in_passengers += get_in_passengers_cycle
    stops_counter += 1
    if stops_counter % 2 == 1:  # if odd
        # if_odd == True
        # if_even == False
        get_in_passengers += 2
    elif stops_counter % 2 == 0:  # if even
        # if_odd == False
        # if_even == True
        get_off_passengers += 2
# Formula to calculate total num of passengers:
final_num_passengers = num_passengers + get_in_passengers - get_off_passengers
print(f"The final number of passengers is : {final_num_passengers}")


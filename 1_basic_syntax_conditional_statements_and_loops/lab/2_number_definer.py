floating_point_num = float(input())
if floating_point_num == 0:
    print("zero")
elif 1 < floating_point_num < 1000000:
    print("positive")
elif 1 > floating_point_num > 0:
    print("small positive")
elif abs(floating_point_num) < 1 and abs(floating_point_num) < 1000000:
    print("negative")
elif abs(floating_point_num) < 1 < abs(floating_point_num):
    print("small negative")
elif floating_point_num > 1000000:
    print("large positive")
elif abs(floating_point_num) > 1000000:
    print("large negative")
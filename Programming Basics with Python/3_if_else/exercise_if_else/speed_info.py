speed = float(input())
#slow
if speed <= 10:
    print("slow")
#average
elif speed <= 50:
    print("average")
#fast
elif speed <= 150:
    print("fast")
#ultra fast
elif speed <= 1000:
    print("ultra fast")
# extremely fast
elif speed > 1000:
    print("extremely fast")

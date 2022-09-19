times = int(input())
cars = set()


def carListCheck(cars, car, io):
    if io == "OUT":
        if cars:
            if car in cars:
                cars.remove(car)
        else:
            pass
            
    elif io == "IN":
        if car in cars:
            pass
        else:
            cars.add(car)
    return cars, car


for i in range(0, times):
    user_input = input().split(", ")
    car = user_input[1]
    io = user_input[0]
    cars, car = carListCheck(cars, car, io)
if cars:
    for each in cars:
        print(each, end="\n")
else: 
    print("Parking Lot is Empty")
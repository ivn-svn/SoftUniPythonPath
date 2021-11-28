destination = input()
savedMoney = 0
while destination != "End":
    neededMoney = float(input())
    while savedMoney <= neededMoney:
        money = float(input())
        savedMoney += money
        if savedMoney >= neededMoney:
            print(f"Going to {destination}!")
            break
    savedMoney = 0
    destination = input(
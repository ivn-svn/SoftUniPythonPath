command = input()
sum_numbers = 0
while command != "Stop":
    integernums = int(command)
    sum_numbers += integernums
    command = input()
print(sum_numbers)
    # try:
    #     integernums = int(input())
    # except:
    #     print("The program has stopped reading integer numbers.")

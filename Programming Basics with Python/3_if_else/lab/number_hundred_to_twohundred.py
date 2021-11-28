# Да се напише програма, която чете цяло число, въведено от потребителя, и проверява, дали е под 100,
# между 100 и 200 или над 200. Да се отпечатат съответно съобщения, като в примерите по-долу:
integer = int(input())
if integer > 200:
    print("Greater than 200")
elif integer <= 200 and integer >= 100:
    print("Between 100 and 200")
elif integer < 100:
    print("Less than 100")



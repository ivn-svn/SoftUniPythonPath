# В таблицата са посочени основните видове суши и ресторантите, които го предлагат, както и цената за порция суши.
# Ако искате да си поръчате за вкъщи се доплаща цена за доставка, която е на стойност 20 % от цялата поръчка.
#
# Напишете програма, която изчислява колко ще е цената за поръчката. При въвеждане на невалиден ресторант да се отпечатва:
# {име на ресторанта} is invalid restaurant!
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
#     • Видът суши –  текст  –  една от възможностите: "sashimi", "maki", "uramaki", "temaki"
#     • Име на ресторанта – текст – една от възможностите: "Sushi Zone", "Sushi Time", "Sushi Bar", "Asian Pub"
#     • Брой порции – цяло число в интервала [1…100]
#     • Поръчка – символ – 'Y' или 'N'
# Изход
# Да се отпечата на конзолата :
#     • Total price: {крайна цена} lv.
# където резултатът трябва да бъде закръглен до по-голямото цяло число.
import math
sushi_portion = 0
take_away = 0.2
# I N P U T :
sushi = input()
restaurant = input()
portions = int(input())
order = input()
# Price  calculation:
price = 0
# Restaurant checkup
if restaurant == "Sushi Zone" or restaurant == "Sushi Time" or restaurant == "Sushi Bar" or restaurant == "Asian Pub":
    # Sushi zone
    if sushi == "sashimi" and restaurant == "Sushi Zone":
        price += 4.99
    elif sushi == "maki" and restaurant == "Sushi Zone":
        price += 5.29
    elif sushi == "uramaki" and restaurant == "Sushi Zone":
        price += 5.99
    elif sushi == "temaki" and restaurant == "Sushi Zone":
        price += 4.29
    # Sushi Time
    elif sushi == "sashimi" and restaurant == "Sushi Time":
        price += 5.49
    elif sushi == "maki" and restaurant == "Sushi Time":
        price += 4.69
    elif sushi == "uramaki" and restaurant == "Sushi Time":
        price += 4.49
    elif sushi == "temaki" and restaurant == "Sushi Time":
        price += 5.19
    # Sushi Bar
    elif sushi == "sashimi" and restaurant == "Sushi Bar":
        price += 5.25
    elif sushi == "maki" and restaurant == "Sushi Bar":
        price += 5.55
    elif sushi == "uramaki" and restaurant == "Sushi Bar":
        price += 6.25
    elif sushi == "temaki" and restaurant == "Sushi Bar":
        price += 4.75
    # Asian Pub
    elif sushi == "sashimi" and restaurant == "Asian Pub":
        price += 4.50
    elif sushi == "maki" and restaurant == "Asian Pub":
        price += 4.80
    elif sushi == "uramaki" and restaurant == "Asian Pub":
        price += 5.50
    elif sushi == "temaki" and restaurant == "Asian Pub":
        price += 5.50
    # Check if ordered for home:
    if order == 'Y':
        ordered = take_away * portions * price
        price = price * portions + ordered
    elif order == 'N':
        price = price * portions
    # Print out the price.
    print(f'Total price: {math.ceil(price)} lv.')
else:
    print(f'{restaurant} is invalid restaurant!')



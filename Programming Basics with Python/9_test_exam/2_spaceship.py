# Георги трябва да построи космически кораб, който да събира част от екипажа му.
# За целта, той трябва да го направи така, че да има място за поне трима астронавти, но за не повече от 10.
# Всеки астронавт се нуждае от малка стая, която да е с размери: 2 метра ширина,
# 2 метра дължина и с 40 см по-висока от средната височина на астронавтите.
# Напишете програма, която изчислява обема на кораба, колко астронавта ще събере и принтира на конзолата дали
# той е достатъчно голям.
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
#     • На първия ред е широчината на кораба - реално число в интервала [1.00... 10.00]
#     • На втория ред е  дължината на кораба - реално число в интервала [1.00…10.00]
#     • На третия ред е височината на кораба - реално число в интервала [1.00…20.00]
#     • На четвъртия ред е средната височина на астронавтите  -  реално число в интервала [1.50 … 1.90]
# Изход
# Да се отпечата на конзолата един ред:
#     • Ако броят на астронавтите е между 3 и 10:
# "The spacecraft holds {броя на астронавтите} astronauts."
#     • Ако  броят на астронавтите е по-малък от 3:
#  "The spacecraft is too small."
#     • Ако  броят на астронавтите е по-голям от 10:
# "The spacecraft is too big."
#
# Variables:
import math
astronauts_num = 0
# Input:
ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
avg_astronaut_height = float(input())
# Average astronaut height checkup:
avg_astronaut_height_checkup = avg_astronaut_height + 0.40
# Astronaut room needed:
room_per_astronaut = avg_astronaut_height_checkup * 2 * 2
# Spacecraft volume:
spacecraft_volume = ship_height * ship_length * ship_width
#
astronauts_num = math.floor(spacecraft_volume / room_per_astronaut)
# Output:
if astronauts_num > 3 and astronauts_num < 10:
    print(f'The spacecraft holds {astronauts_num} astronauts.')
elif astronauts_num < 3:
    print('The spacecraft is too small.')
elif astronauts_num > 10:
    print('The spacecraft is too big.')

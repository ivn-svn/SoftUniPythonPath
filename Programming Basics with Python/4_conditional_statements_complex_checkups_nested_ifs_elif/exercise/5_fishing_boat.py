#     5. Лодка за риболов
# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова, че решават да отидат на риболов
# с кораб. Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
#     • Цената за наем на кораба през пролетта е  3000 лв.;
#     • Цената за наем на кораба през лятото и есента е  4200 лв.;
#     • Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
#     • Ако групата е до 6 човека включително  –  отстъпка от 10%;
#     • Ако групата е от 7 до 11 човека включително  –  отстъпка от 15%;
#     • Ако групата е от 12 нагоре  –  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна
# отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# Вход
# От конзолата се четат три реда:
#     • Бюджет на групата – цяло число;
#     • Сезон –  текст: "Spring", "Summer", "Autumn" или "Winter";
#     • Брой рибари – цяло число.
# Изход
# На конзолата да се отпечата следното:
#     • Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
#     • Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая
# User Inputs:
group_budget = int(input())
season = str(input().lower())
group_members = int(input())
#
ship_price = 0
discount = 0
money_left = 0
#
if season == "summer" or season == "autumn":
    ship_price = 4200
elif season == "winter":
    ship_price = 2600
elif season == "spring":
    ship_price = 3000
else:
    pass
if group_members <= 6:
    discount = 0.1
#
elif 7 <= group_members <= 11:
    discount = 0.15
#
elif group_members >= 12:
    discount = 0.25
    #
else:
    pass
if season != "autumn" and group_members % 2 == 0:
    ship_price = ship_price - ship_price * discount
    ship_price *= 0.95
else:
    ship_price = ship_price - ship_price * discount # 4200 - 630
if ship_price <= group_budget: # 4200 > 3570
    money_left = abs(ship_price - group_budget)
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_left = abs(group_budget - ship_price)
    print(f"Not enough money! You need {money_left:.2f} leva.")
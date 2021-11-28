# На осемнадесетия си рожден ден Хосе взел решение, че ще се изнесе да живее на квартира.
# Опаковал багажа си в кашони и намерил подходяща обява за апартамент под наем.
# Той започва да пренася своя багаж на части, защото не може наведнъж.
# Има ограничено свободно пространство в новото си жилище, където може да разположи вещите,
# така че мястото да бъде подходящо за живеене.
# Напишете програма, която изчислява свободния обем от жилището на Хосе, който остава, след като пренесе багажа си.
# Всеки кашон е с точни размери:  1m x 1m x 1m.
#
# Потребителят въвежда следните данни на отделни редове:
#     1. Широчина на свободното пространство - цяло число;
#     2. Дължина на свободното пространство - цяло число;
#     3. Височина на свободното пространство - цяло число;
#     4. На следващите редове (до получаване на команда "Done") - брой кашони,
#     които се пренасят в квартирата - цели числа
# Програмата трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.
#
# Изход
# Да се отпечата на конзолата един от следните редове:
#     • Ако стигнете до командата "Done" и има още свободно място:
# "{брой свободни куб. метри} Cubic meters left."
#     • Ако свободното място свърши преди да е дошла команда "Done":
# "No more free space! You need {брой недостигащи куб. метри} Cubic meters more."
width = int(input())
length = int(input())
height = int(input())
space_volume = width * length * height
free_space = space_volume
is_done_moving = False
while free_space > 0:
    command = input()
    if command == "Done":
        is_done_moving = True
        break
    boxes_count = int(command)
    free_space -= boxes_count
if is_done_moving:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
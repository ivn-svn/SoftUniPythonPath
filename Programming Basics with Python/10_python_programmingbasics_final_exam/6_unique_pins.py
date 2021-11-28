# Да се напише програма, която генерира трицифрени PIN кодове, като цифрите на всеки PIN код са в определен
# интервал. За да бъде валиден един PIN код той трябва да отговаря на следните условия:
#     • Първата и третата цифра трябва да бъдат четни.
#     • Втората цифра трябва да бъде просто число в диапазона [2...7].
# Вход
# От конзолата се четат 3 реда:
#     • Горната граница на първото число - цяло число в диапазона [1...9]
#     • Горната граница на второто число - цяло число в диапазона [1...9]
#     • Горната граница на третото число - цяло число в диапазона [1...9]
# Изход
# Да се отпечатат на конзолата всички валидни трицифрени PIN кодове, чиито цифри отговарят на съответните интервали.
# INPUT
upper_limit1 = int(input())
upper_limit2 = int(input())
upper_limit3 = int(input())
ranger = [2, 3, 5, 7]
# Code to check range:
if upper_limit1 and upper_limit2 and upper_limit3 in range(1, 9):
    for x in range(1, upper_limit1 + 1):
        if x % 2 != 0:
            continue
        else:
            for y in range(1, upper_limit2 + 1):
                if y not in ranger:
                    continue
                else:
                    for z in range(1, upper_limit3 + 1):
                        if z % 2 != 0:
                            continue
                        else:
                            print(f"{x} {y} {z}")
# Generated pins
# pin_gen = 0

# else:
#     print(" ")

# От конзолата се прочитат 3 реда, въведени от потребителя:
# # #     • N1 – цяло число;
# # #     • N2 – цяло число;
# # #     • Оператор – един символ измежду: "+", "-", "*", "/", "%".

# Изход
# Да се отпечата на конзолата един ред:
#     • Ако операцията е събиране, изваждане или умножение:
#         ◦  "{N1} {оператор} {N2} = {резултат} – {even/odd}"
#     • Ако операцията е деление:
#         ◦ "{N1} / {N2} = {резултат}" – резултат, форматиран до втория знак след десетичната запетая
#     • Ако операцията е модулно деление:
#         ◦ "{N1} % {N2} = {остатък}"
#     • В случай на деление с 0 (нула):
#         ◦ "Cannot divide {N1} by zero"
# Напишете програма, която чете две цели числа (N1 и N2) и оператор, с който да се извърши дадена
# математическа операция.                                                                   [X]
#
# Възможните операции са: Събиране(+), Изваждане(-), Умножение(*),
# Деление(/) и Модулно деление(%).                                                          [X]
#
# При събиране, изваждане и умножение на конзолата трябва да се
# отпечатат резултата и дали той е четен или нечетен.                                       [X]
#
# При обикновеното деление – резултата. При
# модулното деление – остатъка. Трябва да се има предвид, че делителят може да е равен на 0 (нула), а на
# нула не се дели. В този случай трябва да се отпечата специално съобщениe.                 [X]
#
from contextlib import suppress
n1 = int(input())
n2 = int(input())
operator = str(input())
result = 0
if operator == "%" and n2 != 0:
    result = n1 % n2
    print(f"{n1} % {n2} = {result}")
elif operator == "%" and n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == "/" and n2 != 0:
    result = n1 / n2
    print(f"{n1} / {n2} = {result:.2f}")
elif operator == "/" and n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif n2 == 0:
    print(f"Cannot divide {n1} by zero")



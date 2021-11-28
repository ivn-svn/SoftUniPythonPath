# Напишете програма, която чете n-на брой числа, въведени от потребителя, и пресмята сумата,
# минимума и максимума на числата на четни и нечетни позиции (броим от 1).
# Когато няма минимален / максимален елемент, отпечатайте "No".
# Изходът да се форматира в следния вид:
# "OddSum=" + {сума на числата на нечетни позиции},
# "OddMin=" + { минимална стойност на числата на нечетни позиции } / {“No”},
# "OddMax=" + { максимална стойност на числата на нечетни позиции } / {“No”},
# "EvenSum=" + { сума на числата на четни позиции },
# "EvenMin=" + { минимална стойност на числата на четни позиции } / {“No”},
# "EvenMax=" + { максимална стойност на числата на четни позиции } / {“No”}
# Всяко число трябва да е форматирано до втория знак след десетичната запетая.
import sys
n = int(input())
odd_sum = 0
odd_max = sys.maxsize
odd_min = sys.maxsize
#
even_sum = 0
even_max = sys.maxsize
even_min = -sys.maxsize
for i in range(1, n + 1):
    current_num = float(input())
    if i % 2 == 0:
        even_sum += current_num
        if current_num < even_min:
            even_min = current_num
        elif current_num > even_max:
            even_max = current_num
    else:
        odd_sum += current_num
        if current_num > odd_max:
            odd_max = current_num
        elif current_num < odd_min:
            odd_min = current_num
print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min:.2f},")
print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min:.2f},")
print(f"EvenMax={even_max:.2f}")
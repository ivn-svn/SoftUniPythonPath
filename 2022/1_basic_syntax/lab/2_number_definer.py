inputed_num = float(input())
num_definer = ''
if inputed_num == 0:
    num_definer += 'zero'
elif 0 < inputed_num < 1000000:
    num_definer += 'positive'
elif 0 > inputed_num > -1000000:
    num_definer += 'negative'
elif inputed_num > 1000000:
    num_definer += 'large positive'
elif inputed_num < -1000000:
    num_definer += 'large negative'
elif abs(inputed_num) < 1:
    num_definer += 'small'
elif inputed_num < 0:
    num_definer += 'negative'
elif 0 > inputed_num > -1:
    num_definer += 'small negative'
elif 0 < inputed_num < 1:
    num_definer += 'small positive'
print(num_definer)
# zero
# positive
# negative
# small
# large
# Задачата е все още грешна.
input_str = input()
list_input_str = [x for x in input_str]
from_list_repeat = ''
word_repeat = []
if " " in list_input_str:
    word_repeat = input_str.split(" ")
    for z in word_repeat:
        from_list_repeat += z * len(z)
    print(from_list_repeat)
else:
    n = len(input_str)
    concat_str_list = ''
    repeated = input_str * n
    print(repeated)

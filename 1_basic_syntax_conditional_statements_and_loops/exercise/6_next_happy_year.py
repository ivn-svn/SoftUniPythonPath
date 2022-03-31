year_input = int(input())
isFound = False
index_counter = 0
year_str = str(year_input)
year_concat = ''
while isFound == False:
    for x in year_str:
        digit = (year_str)[index_counter]
        index_counter += 1

    year_concat += digit
    while digit not in year_concat:
        pass
    else:
        digit = int((year_str)[index_counter])
        digit += 1
        digit = str(digit)
        year_concat += digit

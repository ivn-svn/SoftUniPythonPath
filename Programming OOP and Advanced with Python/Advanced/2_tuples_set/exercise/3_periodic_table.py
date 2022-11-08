elements = set()
n = int(input())
for line in range(0, n):
    user_input = input()
    elements_list = user_input.split(' ')

    for el in elements_list:
        elements.add(el)

for print_el in elements:
    print(print_el, end='\n')


# 4
# Ce O
# Mo O Ce
# Ee
# Mo

# keep unique periodic table chemical elements only from the line by line input above
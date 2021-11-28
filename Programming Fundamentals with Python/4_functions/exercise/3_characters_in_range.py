a = input()
b = input()


def find_ascii_chr(a, b):
    a_asci_ord_print = ord(f'{a}')
    b_asci_ord_print = ord(f'{b}')
    # return find_range
    # find_ascii_chr(a, b)
    # def print_range_a_b():
    for i in range(a_asci_ord_print  + 1, b_asci_ord_print):
        # return i
        print(chr(i), end=' ')


find_ascii_chr(a, b)

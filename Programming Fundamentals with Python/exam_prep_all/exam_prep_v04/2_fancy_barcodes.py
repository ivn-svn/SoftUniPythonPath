# https://judge.softuni.org/Contests/Practice/Index/2303#1
import re

pat1 = "@#+([A-Z]+[A-z|0-9]+)@#+"
pat2 = "\d+"
barcodes = []
travel_points = 0

matchprod_group = {}


def find_matches(pat, usrinp):
    pattern = re.compile(pat)
    ms = re.findall(pattern, usrinp)
    return ms


n = int(input())

for i in range(0, n):
    user_input = input()
    matches = find_matches(pat1, user_input)
    if matches == []:
        print("Invalid barcode")
    else:
        for match in matches:
            if match != '' and len(match) >= 6:
                barcodes.append(match)
                product_group = find_matches(pat2, match)
                if len(product_group) > 1:
                    group = str(''.join(product_group))
                    print(f"Product group: {group}")

                elif len(product_group) == 1:
                    group = ''.join(product_group)
                    print(f"Product group: {group}")

                elif len(product_group) == 0:
                    group = "00"
                    print(f"Product group: {group}")

                matchprod_group[match] = group

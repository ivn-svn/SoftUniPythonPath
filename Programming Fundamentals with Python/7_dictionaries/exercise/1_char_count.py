input_chars = input().split()
joined_chars = "".join(input_chars)
list_sep_chars = [x for x in joined_chars]
unique_chars = set(list_sep_chars)
for y in unique_chars:
    ccounter = list_sep_chars.count(y)
    print(f"{y} -> {ccounter}")



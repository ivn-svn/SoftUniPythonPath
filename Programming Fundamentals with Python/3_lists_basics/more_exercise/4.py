num_list = input()
k = int(input())
num_list1 = [int(num) for num in num_list if num != ' ']

def josephus(ls, skip):
    skip -= 1 # pop automatically skips the dead guy
    idx = skip
    final_list = []
    while len(ls) > 1:
        final_list.append(ls.pop(idx)) # kill prisoner at idx
        idx = (idx + skip) % len(ls)
    final_list.append(ls[0])
    print(final_list)
josephus(num_list1, k)
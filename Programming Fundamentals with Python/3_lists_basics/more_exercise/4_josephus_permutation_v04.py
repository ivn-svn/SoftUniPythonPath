s_list = input().split(' ')
k = int(input())
#
soldiers_list = [int(x) for x in s_list]
def josephus(ls, skip):
    skip -= 1 # pop automatically skips the dead guy
    idx = skip
    while len(ls) > 1:
        print(ls.pop(idx)) # kill prisoner at idx
        idx = (idx + skip) % len(ls)
    print('survivor: ', ls[0])
josephus(soldiers_list, k)
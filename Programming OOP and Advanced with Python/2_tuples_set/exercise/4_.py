user_input = input()
set_letters = set(list(user_input))
alphabetically_sorted_set = sorted(set_letters)
for letter in alphabetically_sorted_set:
    times = list(user_input).count(letter)
    print(f'{letter}: {times} time/s')


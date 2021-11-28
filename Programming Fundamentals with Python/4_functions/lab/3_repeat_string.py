str_func = str(input())
how_many_times = int(input())


def repeat_n(str, n):
    repeated_string = str_func * how_many_times
    return repeated_string


print(repeat_n(str_func, how_many_times))

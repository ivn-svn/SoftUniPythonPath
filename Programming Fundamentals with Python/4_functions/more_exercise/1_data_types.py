user_input = input()


def inp_func(usr):
    if usr.lower() == "int":
        int_inp = int(input())
        int_inp *= 2
        return int_inp
    elif usr.lower() == "real":
        real_inp = float(input())
        real_inp *= 1.50
        return f"{real_inp:.2f}"
    elif usr.lower() == "string":
        string_inp = "$" + str(input()) + "$"
        return string_inp


printable = inp_func(user_input)

print(f"{printable}")

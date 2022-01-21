n = input()
h = input()
def chars_range(a, b):
    a= ord(n)
    b = ord(h)
    for i in range(a + 1, b):
        z = chr(i)
        print(z, end=' ')
chars_range(n, h)
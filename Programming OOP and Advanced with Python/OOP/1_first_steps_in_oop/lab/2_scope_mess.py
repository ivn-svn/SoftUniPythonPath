import xdrlib


x = "global"

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)
    def change_global():
        x = "global: changed!"
        print(x)
    def outer():
        x = "nonlocal"
        print(f"outer: {x}")

    print("outer:", x) 
    inner() 
    outer()
    change_global() 
print(x) 
outer() 

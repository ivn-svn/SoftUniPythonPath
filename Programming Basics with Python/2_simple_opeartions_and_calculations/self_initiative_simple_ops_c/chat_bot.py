import winsound
#
def my_function():
    winsound.Beep(1000, 150)
    print("This is a beeping sound")

name = str(input())

if name != "h.i":
    my_function()
else:
    print("the dot is a hidden 'u'")
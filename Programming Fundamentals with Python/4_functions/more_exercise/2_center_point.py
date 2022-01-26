#  2. You will be given the coordinates of two points on a Cartesian coordinate
#  system - X1, Y1, X2, and Y2 on separate lines.
#  Write a function that prints the point which is closest to the center of the coordinate
#  system (0, 0) in the format: "({X}, {Y})"
#  If the points are at the same distance from the center, print only the first one.
#  The resulting coordinates must be formatted to the lower integer.
#
#
cords_dict = {}
def coord_func(fst, scd):
    if fst < scd:
        if x1 == y1:
            print(f"({x1:.0f}")

        else:
            print(f"({x1:.0f}, {y1:.0f})")
    else:
        if x2 == y2:
            print(f"({x2:.0f}")
        else:
            print(f"({x2:.0f}, {y2:.0f})")


#
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
#
first = abs(float(x1)) + abs(float(y1))
second = abs(float(x2)) + abs(float(y2))

#
if coord_func(first, second) == None:
    pass
else:
    print(coord_func(first, second))

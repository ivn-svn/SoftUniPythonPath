x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
#
is_on_left_side = x == x1 and y1 <= y <= y2
is_on_right_side = x == x2 and y1 <= y <= y2
is_on_top_side = y == y1 and x1 <= x <= x2
is_on_bottom_side = y == y2 and x1 <= x <= x2
#
if is_on_bottom_side or is_on_right_side or is_on_top_side or is_on_left_side:
    print("Border")
else:
    print("Inside / Outside")
# Дадени са n цели числа в интервала [1…1000].
# От тях някакъв процент p1 са под 200, друг процент p2 са от 200 до 399,
# друг процент p3 са от 400 до 599, друг процент p4 са от 600 до 799
# и останалите p5 процента са от 800 нагоре. Да се напише програма,
# която изчислява и отпечатва процентите p1, p2, p3, p4 и p5.
import sys
max_num = sys.maxsize
integer_1_1000 = int(input())
percentageof = float()
if integer_1_1000 <= 1000:
    for i in range(0, n):
    usernumber = int(input())
    # p1 = x% range(0, 200)
    # p2 = x% range(200, 399)
    # p3 = x% range(400, 599)
    # p4 = x% range(600, 799)
    # p5 = x% range(800, max_num)
    print(f"{percentageof:.2f}%")
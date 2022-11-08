
from collections import deque
#
food_qty = int(input())
int_seq = deque(input().split(' '))
int_seq_original = int_seq.copy()
int_seq_copy = deque(int_seq.copy())
int_seq_ints = [int(y) for y in int_seq]
#)
served = 0 
print(max(int_seq_ints))
while int_seq:
    order = int_seq.popleft()
    order_int = int(order)
    if order_int <= food_qty:
        food_qty -= order_int
        int_seq_copy.popleft()
        served += 1
    else: 
        break
#
if served == len(int_seq_original):
    print('Orders complete')
else:
    orders_left = [str(x) for x in int_seq_copy]
    orders_left = ' '.join(orders_left)
    #print(food_qty)
    print(f'Orders left: {orders_left}')
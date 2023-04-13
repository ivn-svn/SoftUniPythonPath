from collections import deque



bowls_ramen = deque([int(y) for y in input().split(", ")])
customers = deque([int(z) for z in input().split(", ")])

# b = "14, 25, 37, 43, 19" # TO REMOVE!!!
# c = "58, 23, 37" # TO REMOVE!!!
# b = "30, 13, 45"
# c = "70, 25, 55, 15"
# b = "30, 25"
# c = "20, 35"

# bowls_ramen = deque([int(y) for y in b.split(", ")]) # TO REMOVE!!!
# customers = deque([int(z) for z in c.split(", ")])  # TO REMOVE!!!

while bowls_ramen and customers:
    bowl = bowls_ramen.pop()
    customer = customers.popleft()

    if bowl == customer:
        pass
    elif bowl > customer:
        bowl -= customer
        bowls_ramen.append(bowl)
    elif customer > bowl:
        customer -= bowl
        customers.appendleft(customer)
  
    

if not customers:
    print("Great job! You served all the customers.")

elif not bowls_ramen:
    print("Out of ramen! You didn't manage to serve all customers.")

if bowls_ramen:
    print("Bowls of ramen left: " + ", ".join([str(b) for b in bowls_ramen]))


if customers:
    print("Customers left: " + ", ".join([str(c) for c in customers]))
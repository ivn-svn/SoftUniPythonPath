budget = float(input())
flour = float(input())
eggs = 0.75 * flour
milk = ((0.25 * flour) + flour) / 4
 
cozonacPrice = flour + eggs + milk
 
eggsCount = 0
cozonacsCount = 0
 
while budget >= cozonacPrice:
    budget -= cozonacPrice
    eggsCount += 3
    cozonacsCount += 1
 
    if cozonacsCount % 3 == 0:
        eggsCount -= cozonacsCount - 2
 
print(f"You made {cozonacsCount} cozonacs! Now you have {eggsCount} eggs and {budget:.2f} BGN left.")
inputed = input()
inputed1 = str(inputed)
sumofeven1 = 0
sumofodd1 = 0
def sumof(inp1, sumofeven, sumofodd):
    for x in range(0, len(inp1)):
        elemtoint = int(inp1[x])
        if elemtoint % 2 == 0:
            sumofeven += elemtoint
        elif elemtoint % 2 == 1:
            sumofodd += elemtoint
    return sumofodd
def sumofeven(inp1, sumofeven, sumofodd):
    for x in range(0, len(inp1)):
        elemtoint = int(inp1[x])
        if elemtoint % 2 == 0:
            sumofeven += elemtoint
        elif elemtoint % 2 == 1:
            sumofodd += elemtoint
    return sumofeven
sumofodd = sumof(inputed, sumofodd1, sumofeven1)
sumofeven = sumofeven(inputed, sumofodd1, sumofeven1)
print(f"Odd sum = {sumofodd}, Even sum = {sumofeven}")

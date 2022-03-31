# Create a function that receives three parameters and calculates a result depending on operator.
# The operator can be  'multiply', 'divide', 'add', 'subtract' .
# The input comes as three parameters – two integers and an operator as a string.
def perform_op(grade1, grade2, operator):
    if operator == "multiply":
        return grade1 * grade2
    elif operator == "divide":
        return grade1 // grade2
    elif operator == "add":
        return grade1 + grade2
    elif operator == "subtract":
        return grade1 - grade2


grade1 = int(input())
grade2 = int(input())
operator = input()
print(perform_op(grade1, grade2, operator))

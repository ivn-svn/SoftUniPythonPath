# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# input: 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
input_data = input()
splitedinput = input_data.split(", ")
positives_list = [x for x in splitedinput if int(x) >= 0]
negatives_list = [y for y in splitedinput if int(y) < 0]
even_list = [z for z in splitedinput if int(z) % 2 == 0]
odd_list = [q for q in splitedinput if int(q) % 2 == 1]
print(
    f'''
      Positive: {', '.join(positives_list)}
      Negative: {', '.join(negatives_list)}
      Even: {', '.join(even_list)}
      Odd: {', '.join(odd_list)}
     '''
)


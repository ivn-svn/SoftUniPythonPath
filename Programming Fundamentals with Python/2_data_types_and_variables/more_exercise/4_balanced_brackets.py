#     4. Balanced Brackets
# On the first line, you will receive n – the number of lines, which will follow. 
# On the following n lines, you will receive one of the following:
#     • Opening bracket – "(",
#     • Closing bracket – ")" or
#     • Random string
# Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one. 
# Nested parentheses are not valid, and if, for example, 
# two consecutive opening brackets exist, the expression should be marked as unbalanced. 
# You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.
n = int(input())
concat_str = ""
balanced = False
unbalanced = False
count_duplicate = 0
#
count_open = 0
count_closed = 0
#
for line in range(n):
    etc = input()
    #
    concat_str += etc

count_duplicate_f = concat_str.count("((")
count_duplicate_b = concat_str.count("))")

count_open = concat_str.count("(")
count_closed = concat_str.count(")")
if count_closed == count_open:
    balanced = True
elif count_duplicate_f > 1 or count_duplicate_b > 1:
    unbalanced = True
else:
    unbalanced = True



if unbalanced:
    print("UNBALANCED")
else:
    print("BALANCED")
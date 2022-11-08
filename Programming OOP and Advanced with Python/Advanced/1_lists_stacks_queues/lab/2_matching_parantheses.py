user_input = input()

idx = 0 
lst_user_input = list(user_input)
parentheses_stack = []

for i in lst_user_input:
    if i == "(":
        parentheses_stack.append(idx)
    elif i == ")":
        popped_idx = parentheses_stack.pop()
        current_idx = idx + 1
        to_join = lst_user_input[popped_idx:current_idx]
        printable = ''.join(to_join)
        print(printable, end='\n')
    idx += 1
n = int(input())
stack = []
rev = []

for i in range(n):
    line = input()
    if ' ' in line:
        cmd = int(line.split(' ')[0])
        num = int(line.split(' ')[1])
    else:
        cmd = int(line)
    if cmd == 1:
        stack.append(num)
    elif cmd == 2:
        if stack:
            stack.pop()
    elif cmd == 3:
        print(max(stack))
    elif cmd == 4:
        print(min(stack))

appendix = []

while stack:
    appendable = stack.pop()
        
    appendix.append(str(appendable))        

print(', '.join(appendix))

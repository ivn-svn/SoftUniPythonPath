from collections import deque

queue = deque()

while True:
    command = input()
    if command == 'End':
        len_q = len(queue)
        print(f'{len_q} people remaining.')
        break
    elif command == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)

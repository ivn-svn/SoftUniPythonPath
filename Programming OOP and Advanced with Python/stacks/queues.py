from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
print(queue)
# Terry arrives
# Graham arrives
# First leaves: 'Eric'
# Second leaves: 'John'
# ['Michael', 'Terry', 'Graham']
# class Stack:

class Stack:
    def __init__(self) -> None:
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

s = Stack()

for v in range(5, 10):
    s.push(v)


s.push(1)
print(s.pop())
print(s.peek())
#print(s.count())

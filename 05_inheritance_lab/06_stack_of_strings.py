class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1] if self.data else None

    def is_empty(self):
        if not self.data:
            return True
        return False

    def __str__(self):
        return '[' + ', '.join(str(x) for x in reversed(self.data)) + ']'


s = Stack()

s.push('apple')
s.push('carrot')

print(s.pop())  # Output: 'carrot'
print(s.top())  # Output: 'apple'
print(s)  # Output: ['apple']
s.push('banana')
print(s)  # Output: ['banana', 'apple']
print(s.is_empty())  # Output: False

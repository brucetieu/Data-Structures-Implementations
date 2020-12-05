
'''
Implement a Stack using arrays.
'''
class Stack:
    def __init__(self):
        self.stack = []

    # Check if stack is empty.
    def isEmpty(self):
        return len(self.stack) == 0

    # Push elements onto the stack.
    def push(self, data):
        self.stack.append(data)

    # Remove elements from the stack.
    def pop(self):
        if self.isEmpty():
            return "Stack underflow"
        else:
            self.stack.pop()

    # Get the top element in the stack.
    def peek(self):
        return self.stack[len(self.stack) - 1] if not self.isEmpty() else "Stack is empty"

    # Get the size of the stack.
    def size(self):
        return len(self.stack)

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.pop()
my_stack.pop()

print(my_stack.peek())
print(my_stack.size())
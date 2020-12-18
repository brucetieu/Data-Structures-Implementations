
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
        

'''
Create Node class for building the stack
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
'''
Implement a stack using linked list from scratch.
'''
class AnotherStack:
    def __init__(self):

        # Head node
        self.first = Node()

    '''
    Push an item onto the top of the stack.
    '''
    def push(self, item):
        new_node = Node(item)

        if self.first is None:
            self.first = new_node
        else:
            new_node.next = self.first
            self.first = new_node

    '''
    Remove the most recent item pushed on to the stack and return it.
    '''
    def pop(self):

        # Remove the first node in the stack.
        if self.first is None:
            return None
        else:
            temp = self.first
            self.first = temp.next
        return temp.data

    '''
    Check if the stack is empty by seeing if the first node is pointing to something or not.
    '''
    def isEmpty(self):
        return self.first.next == None

    
# First stack
my_stack = Stack()

# my_stack.push(1)
# my_stack.push(2)
# my_stack.pop()
# my_stack.pop()

# print(my_stack.peek())
# print(my_stack.size())

# The second stack implementation:
a_stack = AnotherStack()


# first -> to -> be -> or -> not -> to -> be -> None
a_stack.push("how")
a_stack.push("is")
a_stack.push("you")
a_stack.push("feeling")
a_stack.push("bro")


print(a_stack.pop()) # bro
print(a_stack.pop()) # feeling
print(a_stack.pop()) # you
print(a_stack.pop()) # is
print(a_stack.pop()) # how

print(a_stack.isEmpty()) # Stack should be empty.


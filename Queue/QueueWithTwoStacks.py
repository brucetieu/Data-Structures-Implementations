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
class Stack:
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

'''
Implement Queue with Double Stack.
'''
class Queue:
    def __init__(self):
        self.input_stack = Stack() # For enqueue
        self.output_stack = Stack() # For dequeue
        self.size = 0 # Size of Queue.

    ''' 
    Add elements to the end of the queue by pushing items onto the input_stack.
    '''
    def enqueue(self, item):
        self.input_stack.push(item)
        self.size += 1

    ''' 
    Remove items from the queue by reversing the input stack and returning the top element.
    '''
    def dequeue(self):

        # If the output stack is empty, we have to pop elements from the input_stack and push them into the output_stack so that the elements are in reverse order. That way when we dequeue, we get the first item in the queue. So a reversed stack = queue.

        if self.output_stack.isEmpty():
            while not self.input_stack.isEmpty():
                top = self.input_stack.pop()
                self.output_stack.push(top)


        # After elements from input_stack are pushed to output_stack, we can just get the top element in the stack.
        if not self.output_stack.isEmpty():
            temp = self.output_stack.pop()
            self.size -= 1
        
        return temp

    def isEmpty(self):
        return self.size == 0


# Test 
myQ = Queue()

myQ.enqueue("hi")
myQ.enqueue("my")
myQ.enqueue("name")
myQ.enqueue("is")
myQ.enqueue("bruce")

print(myQ.dequeue())
print(myQ.dequeue())
print(myQ.dequeue())
print(myQ.dequeue())
print(myQ.dequeue())

print(myQ.isEmpty())

    





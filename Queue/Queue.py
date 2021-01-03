
'''
Implementation of a Queue.
'''
class Queue:
    def __init__(self):
        # Represent a queue as an array / list.
        self.queue = []

    # Add items at the end of the queue.
    def enqueue(self, item):
        self.queue.insert(0, item)
    
    # Remove items from the front of the queue.
    def dequeue(self):
        if self.is_empty():
            print('Queue is already empty, nothing to dequeue')
        else:
            self.queue.pop()

    # Get the first element in the queue.
    def peek(self):
        if self.is_empty():
            print('Queue is already empty, nothing to peek')
        return self.queue[-1]

    # Check if the queue is empty.
    def is_empty(self):
        return len(self.queue) == 0

    # Get the number of elements in the queue.
    def get_size(self):
        return len(self.queue)
    
    
my_q = Queue()

my_q.enqueue("hello")
my_q.enqueue("world")
my_q.enqueue("bye")
my_q.enqueue("people")

my_q.dequeue()  # remove "hello"

print(my_q.peek()) # world
print(my_q.get_size()) # 3


####

'''Implement a Queue with a Linked List'''

class QueueViaLinkedList:

    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head == None
    
    '''Add item to the end of the queue.'''
    def enqueue(self, item):
        new_node = self.Node(item)

        # If the head is null point the head to the new node.
        if self.head is None:
            self.head = new_node
            self.size += 1

        else:
            curr = self.head
            
            while curr.next is not None:
                curr = curr.next

            curr.next = new_node
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty, nothing to remove')
        else:
            temp = self.head.data
            self.head = self.head.next
            self.size -= 1
            return temp

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty, no first element exists')
        else:
            curr = self.head
            return curr.data

    def len(self):
        return self.size

        
newQ = QueueViaLinkedList()
newQ.enqueue("new")
newQ.enqueue("year")
newQ.enqueue("new")
newQ.enqueue("me?")

print(newQ.first())

print(newQ.dequeue())
print(newQ.dequeue())
print(newQ.dequeue())
print(newQ.dequeue())
print(newQ.len())
print(newQ.is_empty())

newQ.enqueue("2021")
print(newQ.first())
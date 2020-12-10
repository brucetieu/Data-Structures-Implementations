
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


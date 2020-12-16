'''
Define a Node class which will go in the queue.
'''
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

'''
Minimum Priority Queue class: an element with low priority is served before an element with high priority
'''
class MinPriorityQueue:
    def __init__(self):
        self.queue = []

    '''
    Insert nodes to the front of the queue.
    '''
    def enqueue(self, node):
        self.queue.insert(0, node)

    
    '''
    Remove items from the queue with the lowest priority.
    '''
    def dequeue(self):
        hashmap = {}

        if self.is_empty():
            print('Queue is already empty, nothing to dequeue')
        else:
            min = float('inf')
            idx = 0

            # Traverse through the queue and locate the node with the lowest priority.
            for i in range(len(self.queue)):
                if self.queue[i].priority < min:
                    min = self.queue[i].priority
                    idx = i
            
            # Remove this from the queue.
            min_priority = self.queue.pop(idx)
            hashmap[min_priority.data] = min_priority.priority
            print("Dequeued:", hashmap)

    ''' 
    Get the first element in the queue.
    '''
    def peek(self):
        hashmap = {}
        if self.is_empty():
            print('Queue is already empty, nothing to peek')
        top = self.queue[-1]
        
        hashmap[top.data] = top.priority
        return hashmap

    '''
    Check if the queue is empty.
    '''
    def is_empty(self):
        return len(self.queue) == 0

    ''' 
    Get the number of elements in the queue.
    '''
    def get_size(self):
        return len(self.queue)


my_min_priorityQ = MinPriorityQueue()

my_min_priorityQ.enqueue(Node("C++", 3))
my_min_priorityQ.enqueue(Node("Python",1))
my_min_priorityQ.enqueue(Node("Java", 15))
my_min_priorityQ.enqueue(Node("C#", 22))
my_min_priorityQ.enqueue(Node("JavaScript", 5))
my_min_priorityQ.enqueue(Node("C", 32))

my_min_priorityQ.dequeue()
my_min_priorityQ.dequeue()
my_min_priorityQ.dequeue()


print("First element in priority queue:", my_min_priorityQ.peek()) 


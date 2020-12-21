'''
 A randomized queue is similar to a stack or queue, except that the item removed is chosen uniformly at random among items in the data structure.
 '''

class RandomizedQueue:
    def __init__(self):
        self.randomized_queue = []
        self.size_of_rand_q = 0

    '''
    Is the randomize queue empty?
    '''
    def isEmpty(self):
        pass

    '''
    Return the number of items on the randomized queue.
    '''
    def size(self):
        return self.size_of_rand_q
    
    '''
    Add the item
    '''
    def enqueue(self, item):
        pass

    '''
    Remove and return a random item
    '''
    def dequeue(self):
        pass

    '''
    Return a random item (but do not remove it)
    '''
    def sample(self):
        pass


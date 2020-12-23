import random

'''
 A randomized queue is similar to a stack or queue, except that the item removed is chosen uniformly at random among items in the data structure. (Use a resizable array)
 '''

class RandomizedQueue:
    def __init__(self):
        self.randomized_queue = []
        self.size_of_rand_q = 0

    '''
    Is the randomize queue empty?
    '''
    def isEmpty(self):
        return self.size() == 0

    '''
    Return the number of items on the randomized queue.
    '''
    def size(self):
        return self.size_of_rand_q
    
    '''
    Add the item
    '''
    def enqueue(self, item):
        self.randomized_queue.append(item)
        self.size_of_rand_q += 1

    '''
    Remove and return a random item
    '''
    def dequeue(self):
        rand_num = random.randint(0, self.size_of_rand_q - 1)
        self.size_of_rand_q -= 1
        x = self.randomized_queue.pop(rand_num)
        return x
        
    '''
    Return a random item (but do not remove it)
    '''
    def sample(self):
        if self.size() > 0:
            return random.choice(self.randomized_queue)

# Test
my_randomQ = RandomizedQueue()

my_randomQ.enqueue("raising canes")
my_randomQ.enqueue("angry chicken")
my_randomQ.enqueue("popeyes")
my_randomQ.enqueue("chik fil a")
my_randomQ.enqueue("churches")

print(my_randomQ.dequeue())
print(my_randomQ.dequeue())
print(my_randomQ.dequeue())
print(my_randomQ.dequeue())

print("random sample:", my_randomQ.sample())

print("size of rand queue:", my_randomQ.size())
print("empty:", my_randomQ.isEmpty())

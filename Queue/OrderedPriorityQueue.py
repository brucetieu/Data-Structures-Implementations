
'''Minimum ordered priority queue class using lists'''
class OrderedPriorityQueue:

    ''' Each element in the priority queue is a node with data and priority.'''
    class Node:
        def __init__(self, data=None, priority=None):
            self.data = data
            self.priority = priority

    def __init__(self):
        self.ordered_p_queue = []

    ''' Insert an item with data and priority into queue in order.'''
    def add(self, data, priority):

        # Create new node.
        new_node = self.Node(data, priority)

        if self.is_empty():
            self.ordered_p_queue.append(new_node)
        else:
            size = self.len()
            j = 0

            # Iterate the j pointer accordingly to insert the node correctly.
            for i in range(size):
                if priority > self.ordered_p_queue[i].priority:
                    j += 1

            self.ordered_p_queue.insert(j, new_node)


    ''' Return a tuple, (k,v), representing the key and value of an
    item in priority queue P with minimum key (but do not remove the item); an error occurs if the priority queue is empty. '''
    def min(self):
        if self.is_empty():
            raise Exception('Priority Queue is empty, nothing to return')
        else:
            return (self.ordered_p_queue[0].data, self.ordered_p_queue[0].priority)

    ''' Remove an item with minimum key from priority queue P,
    and return a tuple, (k,v), representing the key and value of the
    removed item; an error occurs if the priority queue is empty.'''
    def remove_min(self):
        if self.is_empty():
            raise Exception('Priority Queue is empty, no minimum element to remove.')
        else:
            first_ele = self.ordered_p_queue.pop(0)
            return (first_ele.data, first_ele.priority)

    ''' Return True if priority queue P does not contain any items. '''
    def is_empty(self):
        return self.ordered_p_queue == []

    ''' Return the number of items in priority queue P '''
    def len(self):
        return len(self.ordered_p_queue)

    ''' Print out the queues elements.'''
    def printQ(self):
        for i in range(self.len()):
            print(self.ordered_p_queue[i].data, self.ordered_p_queue[i].priority)


orderedPQ = OrderedPriorityQueue()

orderedPQ.add("Alive", 10)
orderedPQ.add("Sore", 8)
orderedPQ.add("Happy", 9)
orderedPQ.add("Dying", 1)
orderedPQ.add("Dead", 0)

print(orderedPQ.remove_min())
print(orderedPQ.remove_min())
print(orderedPQ.remove_min())
print(orderedPQ.remove_min())

print(orderedPQ.min())
print(orderedPQ.len())
print(orderedPQ.is_empty())



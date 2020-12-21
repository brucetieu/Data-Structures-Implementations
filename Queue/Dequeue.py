'''
A double-ended queue or deque (pronounced “deck”) is a generalization of a stack and a queue that supports adding and removing items from either the front or the back of the data structure.
'''

'''
Create Node class for building the Queue. We use doubly linked list.
'''
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prev = None

'''
Use a doubly linked list to create a Dequeue.
'''
class Dequeue:
    def __init__(self):
        self.head = None
        self.last = None
        self.size_of_dq = 0

    '''
    Is the dequeue empty?
    '''
    def isEmpty(self):
        return self.head == None

    '''
    Return the number of items in the dequeue
    '''
    def size(self):
        return self.size_of_dq

    '''
    Add item to front of the dequeue (back of doubly linked list).
    '''
    def addFirst(self, item):
        new_node = Node(item)

        # If head is empty, add the new node.
        if self.head == None:
            self.head = new_node
            self.last = new_node  # Keep track of the last node in the list (the new node will always be the last node).

        else:
            curr = self.head

            # Traverse until we get to the end of the doubly linked list.
            while curr.next != None:
                curr = curr.next

            curr.next = new_node  # Set current pointer to point to new node.
            new_node.prev = curr  # Then keep track of the previous node.
            self.last = new_node  # Point to last node in the list.

        self.size_of_dq += 1  # Add 1 to the size of the dequeue.

    '''
    Add item to back of the dequeue (front of the doubly linked list).
    '''
    def addLast(self, item):
        new_node = Node(item)

        if self.head == None:
            self.head = new_node

        else:
            curr = self.head
            new_node.next = curr
            curr.prev = new_node
            self.head = new_node

        self.size_of_dq += 1

    '''
    Remove and return item from front (back of doubly linked list).
    '''
    def removeFirst(self):

        self.size_of_dq -= 1  # Decrement size of dequeue.

        # If the node to be removed is the last one before the head, return the last item, and remove the node, (so head is none now).
        if self.head.next == None:
            curr = self.head
            self.head = None
            return curr.item

        # Similarly, if previous pointer is not pointing to anything, there's only one node left. So delete the node and return it's data as well.
        if self.last.prev == None:
            temp = self.last.item
            self.head = None
            return temp

        # Otherwise, there are at least 2 items in the dequeue.
        else: 
    
            temp = self.last.item  # Save the item to be deleted so it can be returned.
            temp_last = self.last.prev  # Get the position before the last node.
            temp_last.next = None  # Set it's next pointer to be None.

            # Then set the current's last node prev pointer to be None (effectively deleting the node).
            self.last.prev = None
            self.last = temp_last  # Update the new position of the last pointer. 

        return temp

    '''
    Remove and return the item from the back (front of doubly linked list).
    '''
    def removeLast(self):
        curr = self.head  # Keep track of the head node.

        # If the head doesn't exist, return None as there is nothing to remove.
        if self.head == None:
            return None

        # If there's only one node in the doubly linked list, remove the node and return it's value.
        elif curr.next == None:
            temp = curr.item
            curr = None
            self.size_of_dq -= 1
            return temp

        # There are at least two items in the doubly linked list.
        else:
    
            temp = curr.item

            curr.next.prev = None  # Sever connection of the prev which points to the prev node (the one that's deleted)
            self.head = self.head.next  # Point the head pointer to the node after the node which is being deleted.

            self.size_of_dq -= 1
        
        return temp

# Test dequeue
myDQ = Dequeue()

# monkey -> cat -> dog -> tiger -> elephant -> zebra
myDQ.addFirst("dog")
myDQ.addLast("cat")
myDQ.addFirst("tiger")
myDQ.addFirst("elephant")
myDQ.addFirst("zebra")
myDQ.addLast("monkey")

print(myDQ.removeFirst()) # remove zebra
print(myDQ.removeLast())  # remove monkey
print(myDQ.removeFirst()) # remove elephant
print(myDQ.removeLast())  # remove cat

print(myDQ.size())  # return 2
print(myDQ.isEmpty()) # return False











    

    
        
'''
Create Node class for building the Queue. We use doubly linked list.
'''
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prev = None


# Idea: Maybe use a singly linked list with two pointers: One pointer which keeps track of the head, and another which keeps track of the last node in the list.
class Dequeue:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    '''
    Is the dequeue empty?
    '''
    def isEmpty(self):
        return self.head.next == None

    '''
    Return the number of items in the dequeue
    '''
    def size(self):
        return self.size

    '''
    Add item to front of the dequeue (back of doubly linked list).
    '''
    def addFirst(self, item):
        new_node = Node(item)

        # If head is empty, add the new node.
        if self.head == None:
            self.head = new_node
            self.last = new_node


        else:
            curr = self.head

            # Traverse until we get to the end of the linked list.
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

            # Point to last node in the list.
            self.last = new_node

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

    '''
    Remove and return item from front (back of doubly linked list).
    '''
    def removeFirst(self):

        # If the node to be removed is the last one before the head, return the last item, and remove the node, (so head is none now).

        if self.head.next == None:
            curr = self.head
            self.head = None
            return curr.item

        if self.last.prev == None:
            temp = self.last.item
            self.head = None
            return temp

        # Otherwise, there are at least 2 items in the dequeue.
        else: 
            # Save the item to be deleted so it can be returned.
            temp = self.last.item 

            # Get the position before the last node.
            temp_last = self.last.prev

            # Set it's next pointer to be None.
            temp_last.next = None

            # Then set the current's last node prev pointer to be None (effectively deleting the node).
            self.last.prev = None

            # Update the new position of the last pointer. 
            self.last = temp_last

        return temp

    '''
    Remove and return the item from the back (front of doubly linked list).
    '''
    def removeLast(self):
        curr = self.head

        if self.head == None:
            return None

        elif curr.next == None:
            temp = curr.item
            curr = None
            return temp

        else:
        
            temp = curr.item

            curr.next.prev = None
            self.head = self.head.next
        
        return temp



myDQ = Dequeue()

myDQ.addFirst("dog")
myDQ.addLast("cat")
# myDQ.addFirst("tiger")
# myDQ.addFirst("elephant")
# myDQ.addFirst("zebra")
# myDQ.addLast("monkey")

print(myDQ.removeFirst())
# print(myDQ.removeFirst())
# print(myDQ.removeLast())
# print(myDQ.removeFirst())
# print(myDQ.removeLast())
# print(myDQ.removeFirst())












    

    
        
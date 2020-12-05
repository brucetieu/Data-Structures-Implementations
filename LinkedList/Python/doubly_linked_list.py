
'''
Define a Doubly Linked List node class.
'''
class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

'''
Doubly Linked List class.
'''
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the start of the linked list.
    def insert_at_start(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
        
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # Print the linked list using the next pointer.
    def print_forward(self):
        curr = self.head
        ele = []

        while (curr != None):
            ele.append(curr.data)
            curr = curr.next
        print(ele)

    # Insert at the end of the list.
    def insert_at_end(self, data):
       new_node = Node(data)

       if self.head == None:
           self.head = new_node
       else:
           curr = self.head
            
           while (curr.next != None):
               curr = curr.next
           curr.next = new_node
           new_node.prev = curr

    # Delete a node from the doubly linked list.
    def delete(self, data):
        curr = self.head

        if (curr.next != None):
            # Delete node at the head.
            if curr.data == data:
                self.head = curr.next
                self.head.prev = None
            
            # Node to be deleted is not at the head.
            else:
                while curr.next != None:
                    if curr.data == data:
                        break # we found the node to be deleted
                    curr = curr.next
                
                # If the node was node not found.
                if curr.data != data:
                    print(data, "was not found in the list")
                    return
                
                # The node to be deleted is found, and is somewhere in the list (not at the start and not at the end).
                if curr.next:
                    temp = curr.next
                    temp.prev = curr.prev
                    curr.prev.next = temp
                    curr.next = None
                    curr.prev = None

                # The node is at the end of the list.
                elif curr.next == None:
                    curr.prev.next = None
                    curr.prev = None
    
    # Reverse the linked list by traversing the prev pointer.
    def print_reverse(self):
        curr = self.head
        ele = []

        while (curr.next != None):
            curr = curr.next  # We reached the end of the list

        new_curr = curr

        while (new_curr != None):
            ele.append(new_curr.data)
            new_curr = new_curr.prev
        print(ele)
        

                
my_dll = DoublyLinkedList()

my_dll.insert_at_end(1)
my_dll.insert_at_end(2)
my_dll.insert_at_end(3)
my_dll.insert_at_end(4)
my_dll.insert_at_end(5)

my_dll.delete(3)
# my_dll.delete(3)

my_dll.print_forward()
my_dll.print_reverse()

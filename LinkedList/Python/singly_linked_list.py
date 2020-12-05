class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    # Add node to the end of the list
    def append(self, data):
        new_node = node(data)
        curr = self.head

        while curr.next != None:
            curr = curr.next
        curr.next = new_node 

    # Get the number of nodes in the linked list
    def length(self):
        curr = self.head
        total = 0

        while curr.next != None:
            total += 1
            curr = curr.next
        return total

    # Print the linked list
    def display(self):
        elems = []
        curr_node = self.head

        while curr_node.next != None:
            curr_node = curr_node.next
            elems.append(curr_node.data)
        return elems

    # Extract data from node at a certain index.
    def get(self, index):
        if index >= self.length():
            print("Index is out of range")
            return None
        
        curr_idx = 0
        curr_node = self.head
        
        while True:
            curr_node = curr_node.next

            if curr_idx == index: return curr_node.data
            curr_idx += 1

    # Delete node at an index
    def erase(self, index):
        if index >= self.length():
            print("Error: Erase index is out of range")
            return

        curr_idx = 0
        curr_node = self.head

        while True:
            last_node = curr_node
            curr_node = curr_node.next

            if curr_idx == index:
                last_node.next = curr_node.next
                return
            curr_idx += 1

    # Use three pointers! curr - track current node, prev - track previous node, next - track next node
    def reverse(self):
        curr = self.head
        prev = None
        next = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
    
    def print_reverse(self, node):
        curr = node

        while (curr != None):
            print(curr.data)
            curr = curr.next

            


my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.erase(2)

print(my_list.display())

reverse = my_list.reverse()
my_list.print_reverse(reverse)

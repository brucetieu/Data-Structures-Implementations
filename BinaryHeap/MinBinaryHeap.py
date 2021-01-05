class MinBinaryHeap:
    def __init__(self):
        self._min_binary_heap = []
        self._size = 0

    def bubble_up(self, index):
        '''Bubble element up when a node is inserted.'''

        # Parent of any node in the heap is (p-1) / 2.
        while (index - 1) // 2 >= 0:
            child_idx = index
            parent_idx = (index - 1) // 2

            if self._min_binary_heap[parent_idx] > self._min_binary_heap[child_idx]:
                self._min_binary_heap[child_idx], self._min_binary_heap[
                    parent_idx] = self._min_binary_heap[parent_idx], self._min_binary_heap[child_idx]

            index = parent_idx

    def trickle_down(self, index):
        '''Trickle down element when the minimum node is removed.'''

        while (2 * index) + 1 < len(self._min_binary_heap):
            min_child = self.locate_min_child(index)

            if self._min_binary_heap[index] > self._min_binary_heap[min_child]:
                self._min_binary_heap[index], self._min_binary_heap[min_child] = self._min_binary_heap[min_child], self._min_binary_heap[index]

            index = min_child
            
    def locate_min_child(self, index):
        '''After deleting minimum node, need to locate the next smallest element to be swapped with bigger node.'''
        
        # Right child of parent at p is 2p + 1, left child of parent at p is 2p + 2 (index positions).
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2

        # Choose the smaller node of the light and right childs and get its index.
        if left_child < len(self._min_binary_heap) - 1 and right_child < len(self._min_binary_heap):
            if self._min_binary_heap[left_child] < self._min_binary_heap[right_child]:
                return left_child
            else: 
                return right_child

        # If right child is missing, choose the left child index.
        elif right_child >= len(self._min_binary_heap):
            return left_child


    def insert(self, val):
        '''Insert a node into the minimum binary heap.'''
        if len(self._min_binary_heap) == 0:
            self._min_binary_heap.append(val)
        else:
            self._min_binary_heap.append(val)
            last_idx = len(self._min_binary_heap) - 1
            
            # 'Bubble' up element if heap order is violated.
            self.bubble_up(last_idx)

    def find_min(self):
        '''Get the minimum element in the heap.'''
        if len(self._min_binary_heap) == 0:
            print("Binary heap is empty, no minimum element exists.")
        else: 
            print(self._min_binary_heap[0])

    def remove_min(self):
        '''Remove the minimum element in the heap.'''
        if len(self._min_binary_heap) == 0:
            print("Binary heap is empty, nothing to remove.")

        else:
            temp = self._min_binary_heap[0]
            self._min_binary_heap[0] = self._min_binary_heap[len(self._min_binary_heap) - 1]
            self._min_binary_heap.pop()
            self.trickle_down(0)  # Trickle down node to preserve heap ordering.
            return temp

    def build_heap(self, array):
        pass

    def print_heap(self):
        print(self._min_binary_heap)


my_min_heap = MinBinaryHeap()

my_min_heap.insert(10)
my_min_heap.insert(4)
my_min_heap.insert(15)
my_min_heap.remove_min()
my_min_heap.insert(20)
my_min_heap.insert(0)
my_min_heap.insert(30)
my_min_heap.remove_min()
my_min_heap.remove_min()
my_min_heap.insert(2)
my_min_heap.insert(4)
my_min_heap.insert(-1)
my_min_heap.insert(-3)


my_min_heap.print_heap()

#     -3 
#     / \
#    4  -1
#   / \  / \
#  30 15 20 2

my_min_heap2 = MinBinaryHeap()

items = [17,15,8,9,10,13,6,4,5,3,1]

for item in items:
    my_min_heap2.insert(item)

print(my_min_heap2.remove_min())
print(my_min_heap2.remove_min())

my_min_heap2.print_heap()

        #         4
        #       /   \
        #      5     8
        #     / \   / \
        #    6  10 15 13
        #   / \
        #  17 10






    

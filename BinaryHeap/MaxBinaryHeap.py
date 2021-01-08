class MaxBinaryHeap:

    #------- Private methods ------- #
    def _bubble_up(self, index):
        '''Bubble element up when a node is inserted.'''

        # Parent of any node in the heap is (p-1) / 2.
        while (index - 1) // 2 >= 0:
            child_idx = index
            parent_idx = (index - 1) // 2

            if self._max_binary_heap[parent_idx] < self._max_binary_heap[child_idx]:
                self._swap(child_idx, parent_idx)

            index = parent_idx

    def _trickle_down(self, index):
        '''Trickle down element when the maximum node is removed.'''

        while (2 * index) + 1 < len(self._max_binary_heap):
            max_child = self._locate_max_child(index)

            if self._max_binary_heap[index] < self._max_binary_heap[max_child]:
                self._swap(index, max_child)

            index = max_child

    def _locate_max_child(self, index):
        '''After deleting maximum node, need to locate the next smallest element to be swapped with bigger node.'''

        # Right child of parent at p is 2p + 1, left child of parent at p is 2p + 2 (index positions).
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2

        # Choose the right node of the left and right childs and get its index.
        if left_child < len(self._max_binary_heap) and right_child < len(self._max_binary_heap):
            if self._max_binary_heap[left_child] < self._max_binary_heap[right_child]:
                return right_child
            else:
                return left_child

        # If right child is missing, choose the left child index.
        elif right_child >= len(self._max_binary_heap):
            return left_child

    def _swap(self, i, j):
        self._max_binary_heap[i], self._max_binary_heap[j] = self._max_binary_heap[j], self._max_binary_heap[i]

    # ------ Public methods ------ #
    def __init__(self):
        self._max_binary_heap = []
        self._size = 0

    def insert(self, val):
        '''Insert a node into the maximum binary heap.'''
        if len(self._max_binary_heap) == 0:
            self._max_binary_heap.append(val)
        else:
            self._max_binary_heap.append(val)
            last_idx = len(self._max_binary_heap) - 1

            # 'Bubble' up element if heap order is violated.
            self._bubble_up(last_idx)
        
        self._size += 1

    def find_max(self):
        '''Get the maximum element in the heap.'''
        if len(self._max_binary_heap) == 0:
            print("Binary heap is empty, no maximum element exists.")
        else:
            print(self._max_binary_heap[0])

    def remove_max(self):
        '''Remove the maximum element in the heap.'''
        if len(self._max_binary_heap) == 0:
            print("Binary heap is empty, nothing to remove.")

        else:
            temp = self._max_binary_heap[0]
            self._max_binary_heap[0] = self._max_binary_heap[len(
                self._max_binary_heap) - 1]
            self._max_binary_heap.pop()
            self._size -= 1
            self._trickle_down(0)  # Trickle down node to preserve heap ordering.
            return temp


    def is_empty(self):
        return self._size == 0

    def len(self):
        return self._size

    def print_heap(self):
        print(self._max_binary_heap)


my_max_heap = MaxBinaryHeap()

items = [1,3,5,4,6,13,10,9,8,15,17]

for item in items:
    my_max_heap.insert(item)

print(my_max_heap.remove_max())
print(my_max_heap.remove_max())

my_max_heap.print_heap()



my_max_heap2 = MaxBinaryHeap()

my_max_heap2.insert(10)
my_max_heap2.insert(4)
my_max_heap2.insert(15)
print(my_max_heap2.remove_max())
my_max_heap2.insert(20)
my_max_heap2.insert(0)
my_max_heap2.insert(30)
print(my_max_heap2.remove_max())
print(my_max_heap2.remove_max())
my_max_heap2.insert(2)
my_max_heap2.insert(4)
my_max_heap2.insert(-1)
my_max_heap2.insert(-3)

my_max_heap2.print_heap()





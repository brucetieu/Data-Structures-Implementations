class MinBinaryHeap:
    def __init__(self):
        self._min_binary_heap = []
        self._size = 0

    def bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            if self._min_binary_heap[(index - 1) // 2] > self._min_binary_heap[index]:
                self._min_binary_heap[index], self._min_binary_heap[(index - 1) // 2] = self._min_binary_heap[(index - 1) // 2], self._min_binary_heap[index]
            index = (index - 1) // 2


    def trickle_down(self, index):
        
        while (2 * index) + 2 < len(self._min_binary_heap) or (2 * index) + 1 < len(self._min_binary_heap):
            if self._min_binary_heap[index] > self._min_binary_heap[(2 * index) + 1]:
                self._min_binary_heap[index], self._min_binary_heap[(2 * index) + 1] = self._min_binary_heap[(2 * index) + 1], self._min_binary_heap[index]
                index = (2 * index) + 1
            elif self._min_binary_heap[index] > self._min_binary_heap[(2 * index) + 2]:
                self._min_binary_heap[index], self._min_binary_heap[(2 * index) + 1] = self._min_binary_heap[(2 * index) + 1], self._min_binary_heap[index]
                index = (2 * index) + 2


    def insert(self, val):
        if len(self._min_binary_heap) == 0:
            self._min_binary_heap.append(val)
        else:
            self._min_binary_heap.append(val)
            last_idx = len(self._min_binary_heap) - 1
            self.bubble_up(last_idx)



    def find_min(self):
        if len(self._min_binary_heap) == 0:
            print("Binary heap is empty, no minimum element exists.")
        return self._min_binary_heap[0]

    def remove_min(self):
        if len(self._min_binary_heap) == 0:
            print("Binary heap is empty, nothing to remove.")

        else:
            self._min_binary_heap[0] = self._min_binary_heap[len(self._min_binary_heap) - 1]
            self._min_binary_heap.pop()
            self.trickle_down(0)

    def build_heap(self):
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


#     -3 
#     / \
#    4  -1
#   / \  / \
#  30 15 20 2

my_min_heap.print_heap()



    
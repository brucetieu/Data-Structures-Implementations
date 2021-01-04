class MinBinaryHeap:
    def __init__(self):
        self._min_binary_heap = []
        self._size = 0

    def bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            if self._min_binary_heap[(index - 1) // 2] > self._min_binary_heap[index]:
                self._min_binary_heap[index], self._min_binary_heap[(index - 1) // 2] = self._min_binary_heap[(index - 1) // 2], self._min_binary_heap[index]
            index = (index - 1) // 2


    
    def trickle_down(self):
        pass

    def insert(self, val):
        if len(self._min_binary_heap) == 0:
            self._min_binary_heap.append(val)
        else:
            self._min_binary_heap.append(val)
            last_idx = len(self._min_binary_heap) - 1
            self.bubble_up(last_idx)



    def min_child(self):
        pass

    def remove_min(self):
        pass

    def build_heap(self):
        pass

    def print_heap(self):
        print(self._min_binary_heap)


my_min_heap = MinBinaryHeap()

my_min_heap.insert(10)
my_min_heap.insert(5)
my_min_heap.insert(11)
my_min_heap.insert(7)
my_min_heap.insert(3)
my_min_heap.print_heap()


    
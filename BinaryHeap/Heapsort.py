
class HeapSort:
    def __init__(self, arr):
        self._max_binary_heap = arr
    
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

    def heapify(self, index):
        for i in range(index // 2, -1, -1):
            self._trickle_down(i)



    def print_heap(self):
        print(self._max_binary_heap)
        
    def heap_sort(self, arr):
        pass

arr = [1,16,5,30,27,17,20,2,57,3,90]

heap_sort = HeapSort(arr)


heap_sort.heapify(len(arr) - 1)

heap_sort.print_heap()

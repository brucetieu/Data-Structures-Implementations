
class HeapSort:
    def __init__(self, arr):
        self._max_binary_heap = arr
    
    def _trickle_down(self, index, N):
        '''Trickle down element when the maximum node is removed.'''

        while (2 * index) + 1 < N:
            max_child = self._locate_max_child(index)

            if self._max_binary_heap[index] < self._max_binary_heap[max_child]:
                self._swap(index, max_child)

            index = max_child

    def _locate_max_child(self, index):
        '''After deleting maximum node, need to locate the next smallest element to be swapped with bigger node.'''

        # Right child of parent at p is 2p + 1, left child of parent at p is 2p + 2 (index positions).
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2

        # Choose the max node by comparing which of the left and right nodes of parent is bigger.
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

    def heapify_heapsort(self, index):
        ''' Build max heap from bottom up'''

        N = index

        # The parent of any node is (p-1) / 2. We are starting at the end of the list and building a heap from the bottom up by repeatedly tricking down the smaller node (heapify).
        for i in range((N - 1) // 2, -1, -1):
            self._trickle_down(i, N)
        
        # Heap sort: Swap first and last element, decrement size of heap, then restore heap order
        while N >= 0:
            self._swap(0, N)
            N -= 1
            self._trickle_down(0, N)


    def print_heap(self):
        print(self._max_binary_heap)
        
    def heap_sort(self, arr):
        pass

arr = [1,16,5,30,27,17,20,2,57,3,90]

heap_sort = HeapSort(arr)
heap_sort.heapify_heapsort(len(arr) - 1)

heap_sort.print_heap()

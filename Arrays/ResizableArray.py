import ctypes

class ResizableArray:
    def __init__(self):
        self._size = 0  # The number of elements in the array is currently 0. 
        self._capacity = 1 # Allocate memory to initially hold one element in the array. We can hold at most 1 item at the moment.

        # Create an array capable of holding capacity number of elements.
        self._array = self._create_array(self._capacity)

    def _create_array(self, capacity):
        '''Create an array using ctypes'''

        # ctypes.py_object() is an instance of a type
        return (ctypes.py_object * capacity)()

    def size(self):
        '''Return the number of elements in the array'''
        return self._size

    def capacity(self):
        return self._capacity

    def get_item(self, index):
        '''Get the value of array at a specified index'''
        if 0 <= index <= self._size - 1:
            return self._array[index]
        raise IndexError('Index does not exist')

    def add(self, item):
        '''Add an item to the end of the array'''

        # If the array is full, we have to resize it. This will happen when we try to add a second element to the array.
        if self._size == self._capacity:

            # Resize the array
            self.resize(2 * self._capacity)
        
        # We always add the item to the end. 
        self._array[self._size] = item
        self._size += 1


    def resize(self, new_size):
        '''Resize the array with the following steps: 
        1. Allocate a new array B with larger capacity
        2. Set B[i] = A[i], for i = 0,...,n−1, where n denotes current number of it
        3. Set A = B
        4. Update the capacity of the array.
        '''
        new_array = self._create_array(new_size)

        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_size

# Test the ResizableArray class.
resizable_array = ResizableArray()

resizable_array.add("hello")
resizable_array.add("there")
resizable_array.add("dynamic")
resizable_array.add("test")
resizable_array.add("this will cause array size to double")


print(resizable_array.get_item(0))
print(resizable_array.get_item(1))
print(resizable_array.get_item(2))
print(resizable_array.get_item(3))


print(resizable_array.size())
print(resizable_array.capacity())




    


'''
Create a Hashmap from scratch using arrays.
'''
class Hashmap:
    def __init__(self, max_size = 10):
        self.MAX_SIZE = max_size
        self.hashmap = [None] * self.MAX_SIZE

    '''
    We are hasing the value of the key, a string, to an index.
    '''
    def get_hash(self, key):

        # Formula: sum of each letters ASCII modded by length of the string.
        hash = 0
        for s in key:
            hash += ord(s)
        return hash % len(key)

    '''
    Add key value pair to hashmap.
    '''
    def add(self, key, value):
        
        # Hash the string to an index.
        hashed_key = self.get_hash(key)

        # If key doesn't already exist in hash map, add the key value pair as a list. e.g [[key,value]]
        if self.hashmap[hashed_key] is None:
            self.hashmap[hashed_key] = [key, value]
            return True
        
        # Otherwise, a key already exists in the hash map.
        else:
            for pairs in self.hashmap:
                if pairs is not None:
                    # If the key is a duplicate, replace the duplicate value.
                    if pairs[0] == key:
                        pairs[1] = value
                        return True

            # Otherwise, just append the new [key,value] into the hash map.
            self.hashmap.append([key, value])
            return True

    '''
    Get the value of the key.
    '''
    def get(self, key):
        for pairs in self.hashmap:
            if pairs is not None:
                if pairs[0] == key:
                    return pairs[1]
        return -1 # Not found

    '''
    Remove a pair with the key value specified.
    '''
    def remove(self, key):
        for idx, pairs in enumerate(self.hashmap):
            if pairs is not None:
                if pairs[0] == key:
                    self.hashmap.pop(idx)
                    return True
        return False



# Test hashmap.
myHashMap = Hashmap()

myHashMap.add('1', 1)
myHashMap.add('name', 'bill')
myHashMap.add("Python", '3.8.3')

print(myHashMap.get('1'))
print(myHashMap.get('name'))
print(myHashMap.get("Python"))

myHashMap.remove('1')
myHashMap.remove('name')
myHashMap.remove('Python')

myHashMap.add("Python", 'Code')
print(myHashMap.get('Python'))

'''
Create a Hashmap from scratch using arrays.
'''
class Hashmap:
    def __init__(self):
        self.MAX_SIZE = 10
        self.hashmap = [None] * self.MAX_SIZE

    def get_hash(self, key):
        hash = 0
        for s in key:
            hash += ord(s)
        return hash % len(key)

    def add(self, key, value):
        hashed_key = 0
        
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

    def get(self, key):
        for pairs in self.hashmap:
            if pairs is not None:
                if pairs[0] == key:
                    return pairs[1]
        return -1


myHashMap = Hashmap()

myHashMap.add('1', 1)
myHashMap.add('name', 'bill')
myHashMap.add("Python", '3.8.3')

print(myHashMap.get('1'))
print(myHashMap.get('name'))
print(myHashMap.get("Python"))

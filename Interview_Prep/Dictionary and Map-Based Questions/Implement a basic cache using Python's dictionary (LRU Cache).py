# LRU(Least recently used cache)
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        # Initialize the OrderedDict as the cache storage and set the capacity
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            # Move the key to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]  # Return the value associated with the key
        else:
            return -1  # Key is not in the cache, return -1

    def put(self, key, value):
        if key in self.cache:
            # Move the key to the end to mark it as recently used
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Pop the first (least recently used) item if the cache is full
            self.cache.popitem(last=False)
        
        # Insert or update the key with the new value
        self.cache[key] = value

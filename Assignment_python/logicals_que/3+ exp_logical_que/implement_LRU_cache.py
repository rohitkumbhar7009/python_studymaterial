# Question: Implement a Least Recently Used (LRU) Cache using Python.

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

# Example
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)
print(cache.get(2))  # Output: -1

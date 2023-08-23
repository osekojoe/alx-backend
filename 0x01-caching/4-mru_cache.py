#!/usr/bin/python3
"""
MRU CACHE
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the MRU cache
        """
        super().__init__()
        self.order = []  # To maintain the order of access

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
        """
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.order:
                # Remove the most recently used item (MRU)
                removed_key = self.order.pop()
                self.cache_data.pop(removed_key)
                print("DISCARD:", removed_key)

        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        # Update the order (move the accessed item to the end)
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]

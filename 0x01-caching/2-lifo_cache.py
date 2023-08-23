#!/usr/bin/python3
"""
LIFO CACHE
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the LIFO cache
        """
        super().__init__()
        self.stack = []  # To maintain the order of insertion

    def put(self, key, item):
        """ Add an item in the cache using LIFO algorithm
        """
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.stack:
                # Remove the last item (LIFO)
                removed_key = self.stack.pop()
                self.cache_data.pop(removed_key)
                print("DISCARD:", removed_key)

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

#!/usr/bin/python3
"""
FIFO CACHING
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the FIFO cache
        """
        super().__init__()
        self.queue = []  # To maintain the order of insertion

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm
        """
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.queue:
                # Remove the first item (FIFO)
                removed_key = self.queue.pop(0)
                self.cache_data.pop(removed_key)
                print("DISCARD:", removed_key)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

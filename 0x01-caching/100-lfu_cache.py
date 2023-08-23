#!/usr/bin/python3
"""
LRU CACHING
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the LFU cache
        """
        super().__init__()
        self.freq_count = {}  # To maintain the frequency of access

    def put(self, key, item):
        """ Add an item in the cache using LFU algorithm
        """
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.freq_count.values())
            lfu_items = [
                k for k, v in self.freq_count.items() if v == min_freq]
            if lfu_items:
                lru_key = min(lfu_items, key=lambda k: self.cache_data[k])
                del self.cache_data[lru_key]
                del self.freq_count[lru_key]
                print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.freq_count[key] = 0

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        # Update frequency count and return value
        self.freq_count[key] += 1
        return self.cache_data[key]

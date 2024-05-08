#!/usr/bin/env python3
"""2. LIFO Caching

An implementation of a LIFO cache system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class representing a caching system
    """

    def __init__(self) -> None:
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache

        This method is a noop if key or item is None

            Args:
                key:  the item key
                item: the item to store in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            print("DISCARD:", self.cache_data.popitem()[0])
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache

            Args:
                key: the key identifying the item
            Returns:
                the item from the cache or None if key
                doesn't exist
        """
        if key is None:
            return None
        return self.cache_data.pop(key, default=None)

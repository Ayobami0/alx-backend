#!/usr/bin/env python3
"""1. FIFI Caching

An implementation of a FIFO cache system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
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
        if (not self.cache_data.get(key)
                and len(self.cache_data) >= self.MAX_ITEMS):
            dict_key = next(iter(self.cache_data))
            del self.cache_data[dict_key]
            print("DISCARD:", dict_key)
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
        return self.cache_data.get(key, None)

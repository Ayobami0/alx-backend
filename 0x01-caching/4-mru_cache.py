#!/usr/bin/env python3
"""MRU Caching

An implementation of a MRU cache system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class representing a caching system
    """
    ACCESSED_ORDER = []

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
                and len(self.cache_data) == self.MAX_ITEMS):
            print("DISCARD:", self.cache_data[self.ACCESSED_ORDER[-1]])
        self.__update_access(key)
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
        item = self.cache_data.get(key)

        if item is None:
            return None
        self.ACCESSED_ORDER.remove(key)
        del self.cache_data[key]
        return item

    @classmethod
    def __update_access(cls, key):
        """Updates the access order of the keys in the cache

            Args:
                key: the key
        """
        if key in cls.ACCESSED_ORDER:
            cls.ACCESSED_ORDER.remove(key)
        cls.ACCESSED_ORDER.append(key)

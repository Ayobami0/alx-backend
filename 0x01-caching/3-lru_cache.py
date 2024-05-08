#!/usr/bin/env python3
"""3. LRU Caching

An implementation of a LRU cache system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
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

        if (not self.cache_data.get(key, None) and len(self.cache_data)
                >= self.MAX_ITEMS):
            dictKey = self.ACCESSED_ORDER[0]
            del self.cache_data[dictKey]
            self.ACCESSED_ORDER.remove(dictKey)
            print("DISCARD:", dictKey)

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
        self.__update_access(key)
        return item

    def __update_access(self, key):
        """Updates the access order of the keys in the cache

            Args:
                key: the key
        """
        if key in self.ACCESSED_ORDER:
            self.ACCESSED_ORDER.remove(key)
        self.ACCESSED_ORDER.append(key)

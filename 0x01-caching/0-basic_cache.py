#!/usr/bin/env python3
"""0. Basic dictionary

An implematation of a basic cache system

Typical usage example:
    my_cache = BasicCache()

    my_cache.put("A", "Hello")
    print(my_cache.get("A"))
"""

from base_caching import BaseCaching


class BasicCaching(BaseCaching):
    """A class representing a basic caching system
        """

    def __init__(self) -> None:
        """Initlizer"""
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

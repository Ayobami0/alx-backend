#!/usr/bin/env python3
"""5. LFU Caching

An implementation of a LFU cache system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A class representing a caching system
    """
    FREQ = {}
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
            least = [k for k, v in self.FREQ.items() if v ==
                     min(self.FREQ.values())]
            if len(least) > 1:
                for v in self.ACCESSED_ORDER:
                    if v in least:
                        dictKey = v
                        break
            else:
                dictKey = least[0]

            del self.cache_data[dictKey]
            del self.FREQ[dictKey]
            self.ACCESSED_ORDER.remove(dictKey)

            print("DISCARD:", dictKey)
        self.__update_freq(key)
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
        self.__update_freq(key)
        self.__update_access(key)
        return item

    @classmethod
    def __update_freq(cls, key):
        """Updates the access order of the keys in the cache

            Args:
                key: the key
        """
        val = cls.FREQ.get(key, None)
        if val is not None:
            cls.FREQ[key] = val + 1
        else:
            cls.FREQ.setdefault(key, 0)

    @classmethod
    def __update_access(cls, key):
        """Updates the access order of the keys in the cache

            Args:
                key: the key
        """
        if key in cls.ACCESSED_ORDER:
            cls.ACCESSED_ORDER.remove(key)
        cls.ACCESSED_ORDER.append(key)

#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
            self,
            index: Union[int, None] = None,
            page_size: int = 10,) -> Dict:
        """Gets the index of a truncated data
        """
        if index is not None:
            assert index >= 0 and index < len(self.indexed_dataset())
        else:
            index = 0

        data = []
        i = index
        extra_count = 0

        while i < page_size + index + extra_count:
            if not self.indexed_dataset().get(i, None):
                extra_count += 1
                i += 1
                continue
            data.append(self.indexed_dataset().get(i))
            i += 1

        return {
            "index": index,
            "next_index": i,
            "page_size": page_size,
            "data": data
        }

#!/usr/bin/env python3
"""Helper functions.

contains helper functions for pagination
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Paginates a page

    Args:
        page: the page
        page_size: the size of each page
    Returns:
        a tuple of size two containing a start index and an end index
            corresponding to the range of indexes to return
    """

    s_idx: int = (page - 1) * page_size
    return (s_idx, s_idx + page_size)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

        assert type(page) is int
        assert page > 0
        assert type(page_size) is int
        assert page_size > 0

        pages: Tuple[int, int] = index_range(page, page_size)

        try:
            return self.dataset()[pages[0]: pages[1]]
        except IndexError:
            return []

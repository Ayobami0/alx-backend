#!/usr/bin/env python3
"""Helper functions.

contains helper functions for pagination
"""

from typing import Tuple


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

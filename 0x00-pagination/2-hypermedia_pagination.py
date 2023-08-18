#!/usr/bin/env python3
'''
Implement a get_hyper method that takes the same arguments (and defaults)
 as get_page and returns a dictionary containing the following
 key-value pairs:
    page_size: the length of the returned dataset page
    page: the current page number
    data: the dataset page (equivalent to return from previous task)
    next_page: number of the next page, None if no next page
    prev_page: number of the previous page, None if no previous page
    total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.
'''

import csv
import math
from typing import Any, Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Simple pagination'''
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        csv_len = len(self.dataset())
        start_idx, end_idx = index_range(page, page_size)
        if start_idx >= csv_len:
            return []

        end_idx = min(end_idx, csv_len)

        return self.dataset()[start_idx: end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        '''returns a dictionary containing key-value pairs'''
        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 < total_pages else None
        prev_page = page - 1 if page > 1 else None

        result = {
            "page_size": page_size,
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return result


def index_range(page: int, page_size: int) -> tuple:
    '''return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters'''
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)

#!/usr/bin/env python3
'''
Implement a method named get_page that takes two integer arguments page with
 default value 1 and page_size with default value 10.
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly
 and return the appropriate page of the dataset
 (i.e. the correct list of rows).
If the input arguments are out of range for the dataset, an empty list should
 be returned.
 '''

import csv
import math
from typing import List


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


def index_range(page: int, page_size: int) -> tuple:
    '''return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters'''
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)

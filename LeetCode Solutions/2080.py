from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.freq_map = defaultdict(list)
        for index, value in enumerate(arr):
            self.freq_map[value].append(index)
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.freq_map:
            return 0
        indices = self.freq_map[value]
        left_index = bisect_left(indices, left)
        right_index = bisect_right(indices, right)
        return right_index - left_index
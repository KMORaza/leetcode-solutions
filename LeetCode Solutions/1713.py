from bisect import bisect_left
from typing import List
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        target_index_map = {value: idx for idx, value in enumerate(target)}
        transformed_arr = [target_index_map[x] for x in arr if x in target_index_map]
        def length_of_lis(seq):
            lis = []
            for value in seq:
                pos = bisect_left(lis, value)
                if pos == len(lis):
                    lis.append(value)
                else:
                    lis[pos] = value
            return len(lis)
        lis_length = length_of_lis(transformed_arr)
        return len(target) - lis_length

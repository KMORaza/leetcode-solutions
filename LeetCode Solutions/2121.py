from typing import List
from collections import defaultdict
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        index_map = defaultdict(list)
        n = len(arr)
        result = [0] * n
        for i in range(n):
            index_map[arr[i]].append(i)
        for indices in index_map.values():
            total_indices = len(indices)
            prefix_sum = 0
            for i in range(total_indices):
                result[indices[i]] += indices[i] * i - prefix_sum
                prefix_sum += indices[i]
            suffix_sum = 0
            for i in range(total_indices - 1, -1, -1):
                result[indices[i]] += suffix_sum - indices[i] * (total_indices - 1 - i)
                suffix_sum += indices[i]
        return result
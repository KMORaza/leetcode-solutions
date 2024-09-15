from bisect import bisect_left
from typing import List
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        INF = float('inf')
        modified_array = [-INF] + arr1 + [INF]
        state = [INF] * len(modified_array)
        state[0] = 0
        for i in range(1, len(modified_array)):
            if modified_array[i - 1] < modified_array[i]:
                state[i] = state[i - 1]
            insert_pos = bisect_left(arr2, modified_array[i])
            for k in range(1, min(i, insert_pos) + 1):
                if modified_array[i - k - 1] < arr2[insert_pos - k]:
                    state[i] = min(state[i], state[i - k - 1] + k)
        return -1 if state[-1] == INF else state[-1]

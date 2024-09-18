from typing import List
from collections import defaultdict
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        def compute_min_lengths(arr: List[int]) -> List[int]:
            min_length = [float('inf')] * n
            current_sum = 0
            prefix_sums = {0: -1}
            for i in range(n):
                current_sum += arr[i]
                if current_sum - target in prefix_sums:
                    start_index = prefix_sums[current_sum - target]
                    min_length[i] = i - start_index
                prefix_sums[current_sum] = i
                if i > 0:
                    min_length[i] = min(min_length[i], min_length[i - 1])
            return min_length
        min_len_left = compute_min_lengths(arr)
        reversed_arr = arr[::-1]
        min_len_right = compute_min_lengths(reversed_arr)[::-1]
        min_sum = float('inf')
        for i in range(n - 1):
            if min_len_left[i] < float('inf') and min_len_right[i + 1] < float('inf'):
                min_sum = min(min_sum, min_len_left[i] + min_len_right[i + 1])
        return min_sum if min_sum < float('inf') else -1

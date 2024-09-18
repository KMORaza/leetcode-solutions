from typing import List
import heapq
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                subarray_sums.append(current_sum)
        subarray_sums.sort()
        result = sum(subarray_sums[left - 1:right])
        return result % (10**9 + 7)

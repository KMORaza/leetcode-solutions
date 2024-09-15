from collections import deque
from typing import List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        deq = deque()
        min_length = float('inf')
        for i in range(n + 1):
            while deq and prefix_sum[i] - prefix_sum[deq[0]] >= k:
                min_length = min(min_length, i - deq.popleft())
            while deq and prefix_sum[i] <= prefix_sum[deq[-1]]:
                deq.pop()
            deq.append(i)
        return min_length if min_length != float('inf') else -1

import heapq
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        max_sum = sum(x for x in nums if x > 0)
        A = sorted(abs(x) for x in nums)
        n = len(A)

        if k == 1:
            return max_sum

        pq = [(A[0], 0)]
        kth_smallest = 0

        for _ in range(k - 1):
            curr_sum, idx = heapq.heappop(pq)
            kth_smallest = curr_sum

            if idx + 1 < n:
                heapq.heappush(pq, (curr_sum + A[idx + 1], idx + 1))
                heapq.heappush(pq, (curr_sum - A[idx] + A[idx + 1], idx + 1))

        return max_sum - kth_smallest
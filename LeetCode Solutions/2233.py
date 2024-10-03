from typing import List
import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            smallest = heapq.heappop(nums)
            smallest += 1
            heapq.heappush(nums, smallest)
        x = 10**9 + 7
        product = 1
        for num in nums:
            product = (product * num) % x
        return product

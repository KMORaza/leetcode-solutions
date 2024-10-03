import heapq
from typing import List
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        target = total_sum / 2
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        current_sum = total_sum
        operations = 0
        while current_sum > target:
            largest = -heapq.heappop(max_heap)
            halved = largest / 2
            current_sum -= halved
            heapq.heappush(max_heap, -halved)
            operations += 1
        return operations

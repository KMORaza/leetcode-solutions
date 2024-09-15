from typing import List
import heapq
class Solution:
    def isPossible(self, array: List[int]) -> bool:
        if len(array) == 1:
            return array[0] == 1
        total_sum = sum(array)
        max_heap = [-num for num in array]
        heapq.heapify(max_heap)
        while -max_heap[0] > 1:
            max_val = -heapq.heappop(max_heap)
            remaining_sum = total_sum - max_val
            if remaining_sum == 1:
                return True
            updated_val = max_val % remaining_sum
            if updated_val == 0 or updated_val == max_val:
                return False
            heapq.heappush(max_heap, -updated_val)
            total_sum = total_sum - max_val + updated_val
        return True

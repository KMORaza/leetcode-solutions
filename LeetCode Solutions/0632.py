import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        for i, lst in enumerate(nums):
            heapq.heappush(min_heap, (lst[0], i, 0))
            current_max = max(current_max, lst[0])
        min_range = float('-inf')
        max_range = float('inf')
        while len(min_heap) == len(nums):
            current_min, list_index, element_index = heapq.heappop(min_heap)
            if current_max - current_min < max_range - min_range:
                min_range = current_min
                max_range = current_max
            if element_index + 1 < len(nums[list_index]):
                next_element = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
                current_max = max(current_max, next_element)
            else:
                break
        return [min_range, max_range]

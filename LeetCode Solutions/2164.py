from typing import List
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_indices = nums[0::2]
        odd_indices = nums[1::2]
        even_indices.sort()
        odd_indices.sort(reverse=True)
        result = []
        for i in range(max(len(even_indices), len(odd_indices))):
            if i < len(even_indices):
                result.append(even_indices[i])
            if i < len(odd_indices):
                result.append(odd_indices[i])
        return result
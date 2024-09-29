from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        result = []
        for p, n in zip(positive, negative):
            result.append(p)
            result.append(n)
        return result
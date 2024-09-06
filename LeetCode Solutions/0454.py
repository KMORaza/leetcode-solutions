from typing import List
from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_count = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                sum_count[num1 + num2] += 1
        result = 0
        for num3 in nums3:
            for num4 in nums4:
                target = -(num3 + num4)
                if target in sum_count:
                    result += sum_count[target]
        return result

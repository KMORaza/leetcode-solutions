from typing import List
from collections import Counter
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2) * 6 or len(nums2) > len(nums1) * 6:
            return -1
        count1, count2 = Counter(nums1), Counter(nums2)
        diff = sum(count1[i] * i for i in count1) - sum(count2[i] * i for i in count2)
        if diff == 0:
            return 0
        if diff > 0:
            count1, count2, diff = count2, count1, -diff
        operations = 0
        for i in range(1, 7):
            while diff > 0 and count2[i] > 0:
                count2[i] -= 1
                diff -= i
                operations += 1
        return operations if diff <= 0 else -1

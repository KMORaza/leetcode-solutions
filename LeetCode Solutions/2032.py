from typing import List
from collections import Counter
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        count = Counter()
        for num in set(nums1):
            count[num] += 1
        for num in set(nums2):
            count[num] += 1
        for num in set(nums3):
            count[num] += 1
        return [num for num in count if count[num] > 1]

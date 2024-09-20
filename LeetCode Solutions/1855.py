from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = 0
        j = 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums2[j] >= nums1[i]:
                j += 1
            if j > 0:
                max_dist = max(max_dist, j - 1 - i)
        return max_dist
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1

        n = len(nums1)
        pos_diff = 0
        neg_diff = 0

        for i in range(n):
            diff = nums1[i] - nums2[i]
            if diff % k != 0:
                return -1
            if diff > 0:
                pos_diff += diff // k
            elif diff < 0:
                neg_diff += (-diff) // k

        return pos_diff if pos_diff == neg_diff else -1
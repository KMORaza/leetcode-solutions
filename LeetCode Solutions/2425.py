class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        xor1 = 0
        xor2 = 0

        if n2 % 2 == 1:
            for num in nums1:
                xor1 ^= num

        if n1 % 2 == 1:
            for num in nums2:
                xor2 ^= num

        return xor1 ^ xor2
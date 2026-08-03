class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        consecutive_zeros = 0

        for num in nums:
            if num == 0:
                consecutive_zeros += 1
                count += consecutive_zeros
            else:
                consecutive_zeros = 0

        return count
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        return False
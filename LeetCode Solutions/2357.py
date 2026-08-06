class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique_non_zero = set(num for num in nums if num > 0)
        return len(unique_non_zero)
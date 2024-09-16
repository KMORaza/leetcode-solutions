class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        current_value = 0
        result = []
        for bit in nums:
            current_value = (current_value * 2 + bit) % 5
            result.append(current_value == 0)
        return result

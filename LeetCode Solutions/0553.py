from typing import List
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        result = f"{nums[0]}/("
        result += '/'.join(map(str, nums[1:]))
        result += ")"
        return result

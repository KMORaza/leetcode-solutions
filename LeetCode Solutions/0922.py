from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        result = [0] * len(nums)
        result[::2] = even
        result[1::2] = odd
        return result

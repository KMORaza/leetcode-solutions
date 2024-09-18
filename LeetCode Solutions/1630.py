from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        results = []
        for left, right in zip(l, r):
            subarray = nums[left:right + 1]
            subarray.sort()
            is_arithmetic = True
            common_diff = subarray[1] - subarray[0]
            for i in range(2, len(subarray)):
                if subarray[i] - subarray[i - 1] != common_diff:
                    is_arithmetic = False
                    break
            results.append(is_arithmetic)
        return results

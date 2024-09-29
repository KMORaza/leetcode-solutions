from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_value(num: int) -> int:
            mapped_num = 0
            multiplier = 1
            for digit in reversed(str(num)):
                mapped_num += mapping[int(digit)] * multiplier
                multiplier *= 10
            return mapped_num
        nums_sorted = sorted(nums, key=mapped_value)
        return nums_sorted

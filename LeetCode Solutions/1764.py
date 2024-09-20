from typing import List
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        index = 0
        n = len(nums)
        for group in groups:
            group_size = len(group)
            found = False
            while index <= n - group_size:
                if nums[index:index + group_size] == group:
                    index += group_size
                    found = True
                    break
                index += 1
            if not found:
                return False
        return True

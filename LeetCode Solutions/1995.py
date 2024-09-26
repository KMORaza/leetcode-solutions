from collections import defaultdict
from typing import List
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for d in range(3, n):
            for a in range(d):
                for b in range(a + 1, d):
                    for c in range(b + 1, d):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1
        return count
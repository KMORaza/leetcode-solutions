from typing import List
from itertools import combinations
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        count = 0
        for i in range(len(nums) + 1):
            for subset in combinations(nums, i):
                current_or = 0
                for num in subset:
                    current_or |= num
                if current_or > max_or:
                    max_or = current_or
                    count = 1
                elif current_or == max_or:
                    count += 1
        return count

from typing import List
from collections import Counter
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = Counter()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                count[nums[i + 1]] += 1
        return count.most_common(1)[0][0] if count else -1

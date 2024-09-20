from typing import List
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_count[product] += 1
        count = 0
        for freq in product_count.values():
            count += freq * (freq - 1) * 4
        return count

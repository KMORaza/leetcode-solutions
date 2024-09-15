from typing import List
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = defaultdict(int)
        remainder_count[0] = 1
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k
            result += remainder_count[remainder]
            remainder_count[remainder] += 1
        return result

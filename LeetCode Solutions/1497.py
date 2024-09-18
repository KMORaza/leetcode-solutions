from typing import List
from collections import Counter
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = Counter(num % k for num in arr)
        for remainder in remainder_count:
            if remainder == 0:
                if remainder_count[remainder] % 2 != 0:
                    return False
            elif 2 * remainder == k:
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                complement = (k - remainder) % k
                if remainder_count[remainder] != remainder_count[complement]:
                    return False
        return True

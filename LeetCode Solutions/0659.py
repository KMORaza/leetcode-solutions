from typing import List
from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        subseq_end = Counter()
        for num in nums:
            if count[num] == 0:
                continue
            if subseq_end[num - 1] > 0:
                subseq_end[num - 1] -= 1
                subseq_end[num] += 1
            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                subseq_end[num + 2] += 1
            else:
                return False
            count[num] -= 1
        return True

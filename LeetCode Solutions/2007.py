from typing import List
from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        count = Counter(changed)
        original = []
        for num in sorted(count):
            if count[num] > count[num * 2]:
                return []
            if num == 0:
                original.extend([0] * (count[num] // 2))
            else:
                original.extend([num] * count[num])
            count[num * 2] -= count[num]
        return original

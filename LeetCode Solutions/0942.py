from typing import List
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        result = []
        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            elif char == 'D':
                result.append(high)
                high -= 1
        result.append(low)
        return result

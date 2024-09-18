from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        for i in range(len(s)):
            result[indices[i]] = s[i]
        return ''.join(result)

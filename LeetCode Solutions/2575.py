from typing import List

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        rem = 0

        for ch in word:
            rem = (rem * 10 + int(ch)) % m
            ans.append(1 if rem == 0 else 0)

        return ans
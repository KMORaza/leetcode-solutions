from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s: str) -> bool:
            bitmask = 0
            for char in s:
                bit = ord(char) - ord('a')
                if bitmask & (1 << bit):
                    return False
                bitmask |= (1 << bit)
            return True
        def backtrack(index: int, bitmask: int) -> int:
            max_length = 0
            for i in range(index, len(filtered)):
                if bitmask & filtered[i][1] == 0:
                    new_bitmask = bitmask | filtered[i][1]
                    max_length = max(max_length, bin(new_bitmask).count('1'))
                    max_length = max(max_length, backtrack(i + 1, new_bitmask))
            return max_length
        filtered = []
        for s in arr:
            bitmask = 0
            if is_unique(s):
                for char in s:
                    bitmask |= (1 << (ord(char) - ord('a')))
                filtered.append((len(s), bitmask))
        return backtrack(0, 0)

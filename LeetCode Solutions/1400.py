from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        freq = Counter(s)
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        return odd_count <= k and k <= len(s)

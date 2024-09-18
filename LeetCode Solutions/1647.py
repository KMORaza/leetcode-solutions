from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        seen = set()
        deletions = 0
        for count in freq.values():
            while count > 0 and count in seen:
                count -= 1
                deletions += 1
            seen.add(count)
        return deletions

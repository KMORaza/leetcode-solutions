class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        counts = Counter(s)
        unique_counts = set(counts.values())
        return len(unique_counts) == 1

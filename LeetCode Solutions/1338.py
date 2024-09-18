class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        counts = Counter(arr)
        sorted_counts = sorted(counts.values(), reverse=True)
        total, half_size = 0, len(arr) // 2
        for i, count in enumerate(sorted_counts):
            total += count
            if total >= half_size:
                return i + 1

class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        intervals = []
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            intervals.append((left, right))
        intervals.sort(key=lambda x: (x[0], -x[1]))
        taps_opened = 0
        current_end = 0
        max_reachable = 0
        i = 0
        while current_end < n:
            while i < len(intervals) and intervals[i][0] <= current_end:
                max_reachable = max(max_reachable, intervals[i][1])
                i += 1
            if max_reachable <= current_end:
                return -1
            current_end = max_reachable
            taps_opened += 1
        return taps_opened


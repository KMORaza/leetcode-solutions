class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        if not ranges:
            return 1

        ranges.sort()
        merged = []

        for start, end in ranges:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        n_groups = len(merged)
        return pow(2, n_groups, MOD)
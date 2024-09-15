class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        ones_count = [0] * (n + 1)
        zeros_count = [0] * (n + 1)
        for i in range(1, n + 1):
            ones_count[i] = ones_count[i - 1] + (1 if s[i - 1] == '1' else 0)
        for i in range(n - 1, -1, -1):
            zeros_count[i] = zeros_count[i + 1] + (1 if s[i] == '0' else 0)
        min_flips = float('inf')
        for i in range(n + 1):
            flips = ones_count[i] + zeros_count[i]
            min_flips = min(min_flips, flips)
        return min_flips

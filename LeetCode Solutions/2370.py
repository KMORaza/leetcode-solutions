class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26

        for char in s:
            idx = ord(char) - ord('a')
            max_len = 0
            for j in range(26):
                if abs(j - idx) <= k:
                    max_len = max(max_len, dp[j])
            dp[idx] = max_len + 1

        return max(dp)
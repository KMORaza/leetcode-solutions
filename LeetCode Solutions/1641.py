class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(1, n):
            for i in range(3, -1, -1):
                dp[i] += dp[i + 1]
        return sum(dp)

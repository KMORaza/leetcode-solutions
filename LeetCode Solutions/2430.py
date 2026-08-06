class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return n

        dp = [0] * n
        for i in range(n - 1, -1, -1):
            for length in range(1, (n - i) // 2 + 1):
                if i + 2 * length > n:
                    continue
                if s[i:i + length] == s[i + length:i + 2 * length]:
                    dp[i] = max(dp[i], dp[i + length] if i + length < n else 0)
            dp[i] += 1

        return dp[0]
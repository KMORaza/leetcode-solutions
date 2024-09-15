class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        x = 1000000007
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(max(0, i - len(str(k))), i):
                substring = s[j:i]
                if (substring[0] != '0' and int(substring) <= k):
                    dp[i] = (dp[i] + dp[j]) % x
        return dp[n]

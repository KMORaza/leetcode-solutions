class Solution:
    def distinctSubseqII(self, S: str) -> int:
        MOD = 10**9 + 7
        n = len(S)
        dp = [0] * (n + 1)
        last_occurrence = {}
        dp[0] = 1
        for i in range(1, n + 1):
            char = S[i - 1]
            dp[i] = (2 * dp[i - 1]) % MOD
            if char in last_occurrence:
                dp[i] -= dp[last_occurrence[char] - 1]
                if dp[i] < 0:
                    dp[i] += MOD
            last_occurrence[char] = i
        return (dp[n] - 1) % MOD

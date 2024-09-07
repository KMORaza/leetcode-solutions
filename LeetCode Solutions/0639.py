class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        if s[0] == '*':
            dp[1] = 9
        elif s[0] != '0':
            dp[1] = 1
        for i in range(1, n):
            if s[i] == '*':
                dp[i + 1] = 9 * dp[i] % MOD
                if s[i - 1] == '1':
                    dp[i + 1] = (dp[i + 1] + 9 * dp[i - 1]) % MOD
                elif s[i - 1] == '2':
                    dp[i + 1] = (dp[i + 1] + 6 * dp[i - 1]) % MOD
                elif s[i - 1] == '*':
                    dp[i + 1] = (dp[i + 1] + 15 * dp[i - 1]) % MOD
            else:
                dp[i + 1] = dp[i] if s[i] != '0' else 0
                if s[i - 1] == '1':
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD
                elif s[i - 1] == '2' and s[i] <= '6':
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD
                elif s[i - 1] == '*':
                    if s[i] <= '6':
                        dp[i + 1] = (dp[i + 1] + 2 * dp[i - 1]) % MOD
                    else:
                        dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD
        return dp[n]

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7

        max_distinct = 15

        dp = [[0] * (maxValue + 1) for _ in range(max_distinct)]

        for v in range(1, maxValue + 1):
            dp[1][v] = 1

        for k in range(1, max_distinct - 1):
            for d in range(1, maxValue + 1):
                if dp[k][d] == 0: continue
                for v in range(2 * d, maxValue + 1, d):
                    dp[k + 1][v] = (dp[k + 1][v] + dp[k][d]) % MOD

        ans = 0
        comb = 1
        for k in range(1, min(max_distinct, n + 1)):
            count_k = sum(dp[k][1:]) % MOD
            ans = (ans + count_k * comb) % MOD
            if k < n:
                comb = (comb * (n - k)) % MOD
                comb = (comb * pow(k, MOD - 2, MOD)) % MOD

        return ans
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(1, n + 1):
            if dp[i] > 0:
                start_share = i + delay
                stop_forget = i + forget

                for j in range(start_share, min(stop_forget, n + 1)):
                    dp[j] = (dp[j] + dp[i]) % MOD

        result = 0
        for i in range(max(1, n - forget + 1), n + 1):
            result = (result + dp[i]) % MOD

        return result
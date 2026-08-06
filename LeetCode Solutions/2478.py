class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        def is_prime(c):
            return c in '2357'

        if not is_prime(s[0]) or is_prime(s[-1]):
            return 0

        primes = set('2357')

        dp = [[0] * n for _ in range(k)]

        for i in range(minLength - 1, n):
            if not is_prime(s[i]):
                dp[0][i] = 1

        for p in range(1, k):
            prefix_sum = 0
            for i in range(n):
                if i >= minLength:
                    if not is_prime(s[i - minLength]) and is_prime(s[i - minLength + 1]):
                        prefix_sum = (prefix_sum + dp[p - 1][i - minLength]) % MOD

                if i >= minLength - 1 and not is_prime(s[i]):
                    dp[p][i] = prefix_sum

        return dp[k - 1][n - 1]
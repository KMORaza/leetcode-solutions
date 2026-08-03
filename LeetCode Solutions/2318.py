from math import gcd


class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        if n == 1:
            return 6

        # dp[i][j] = number of sequences of length i ending with (j, k) where k is the previous element
        # dp[last][prev] where last is the last element and prev is the element before last
        dp = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(n + 1)]

        # Initialize base case: sequences of length 2
        for last in range(1, 7):
            for prev in range(1, 7):
                if last != prev and gcd(last, prev) == 1:
                    dp[2][last][prev] = 1

        # Build up sequences of length 3 to n
        for i in range(3, n + 1):
            for last in range(1, 7):
                for prev in range(1, 7):
                    if last != prev and gcd(last, prev) == 1:
                        for prev_prev in range(1, 7):
                            if prev != prev_prev and gcd(prev, prev_prev) == 1 and last != prev_prev:
                                dp[i][last][prev] = (dp[i][last][prev] + dp[i - 1][prev][prev_prev]) % MOD

        result = 0
        for last in range(1, 7):
            for prev in range(1, 7):
                result = (result + dp[n][last][prev]) % MOD

        return result
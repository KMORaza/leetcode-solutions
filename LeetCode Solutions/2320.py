class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        if n == 1:
            return 4

        # Calculate number of ways to arrange houses on one side of the street
        # This follows a Fibonacci pattern because:
        # - If we don't place a house at position i, we have dp[i-1] ways
        # - If we place a house at position i, we can't place at i-1, so we have dp[i-2] ways
        prev2 = 1  # Base case: with 0 plots, there's 1 way (empty arrangement)
        prev1 = 2  # Base case: with 1 plot, there are 2 ways (no house or one house)

        for i in range(2, n + 1):
            curr = (prev1 + prev2) % MOD
            prev2 = prev1
            prev1 = curr

        # Since both sides of the street are independent,
        # the total number of arrangements is (arrangements for one side) squared
        return (prev1 * prev1) % MOD
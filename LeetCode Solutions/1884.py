class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [0] * (n + 1)
        attempts = 0
        while dp[attempts] < n:
            attempts += 1
            dp[attempts] = dp[attempts - 1] + attempts
        return attempts

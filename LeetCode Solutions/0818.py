class Solution:
    def racecar(self, destiny: int) -> int:
        dp = [float('inf')] * (destiny + 1)
        dp[0] = 0
        for i in range(1, destiny + 1):
            x = 0
            j = (1 << x) - 1
            while j < i:
                x += 1
                j = (1 << x) - 1
                for y in range(x):
                    k = (1 << y) - 1
                    if i - (j - k) >= 0:
                        dp[i] = min(dp[i], (x + 1) + (y + 1) + dp[i - (j - k)])
            dp[i] = min(dp[i], x + (1 if i != j else 0) + dp[j - i])
        return dp[destiny]

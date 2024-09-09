class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1.0 if n * 1.0 / 100 >= 1 else 0.71875
        memo = {}
        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            prob = 0.25 * dp(a - 100, b) \
                 + 0.25 * dp(a - 75, b - 25) \
                 + 0.25 * dp(a - 50, b - 50) \
                 + 0.25 * dp(a - 25, b - 75)
            memo[(a, b)] = prob
            return prob
        return dp(n, n)

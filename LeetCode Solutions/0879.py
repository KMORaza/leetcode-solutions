MOD = 10**9 + 7
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1
        for i in range(m):
            g = group[i]
            p = profit[i]
            for members in range(n + 1):
                for profit_value in range(minProfit + 1):
                    dp[i + 1][members][profit_value] = (dp[i + 1][members][profit_value] + dp[i][members][profit_value]) % MOD
                    if members >= g:
                        new_profit = min(profit_value + p, minProfit)
                        dp[i + 1][members][new_profit] = (dp[i + 1][members][new_profit] + dp[i][members - g][profit_value]) % MOD
        result = 0
        for members in range(n + 1):
            for profit_value in range(minProfit, minProfit + 1):
                result = (result + dp[m][members][profit_value]) % MOD
        return result

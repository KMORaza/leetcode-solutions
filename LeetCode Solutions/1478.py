from typing import List
import bisect
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2
                for x in range(i, j + 1):
                    cost[i][j] += abs(houses[x] - houses[mid])
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for x in range(i):
                    dp[i][j] = min(dp[i][j], dp[x][j - 1] + cost[x][i - 1])
        return dp[n][k]

class Solution:
    def minCost(self, houses, cost, m, n, target):
        LARGE_NUMBER = float('inf')
        dp = [[[LARGE_NUMBER] * (target + 1) for _ in range(n + 1)] for _ in range(m)]
        if houses[0] == 0:
            for color in range(1, n + 1):
                dp[0][color][1] = cost[0][color - 1]
        else:
            dp[0][houses[0]][1] = 0
        for i in range(1, m):
            if houses[i] == 0:
                for current_color in range(1, n + 1):
                    for num_neighborhoods in range(1, min(target, i + 1) + 1):
                        for prev_color in range(1, n + 1):
                            if current_color == prev_color:
                                dp[i][current_color][num_neighborhoods] = min(
                                    dp[i][current_color][num_neighborhoods],
                                    dp[i - 1][current_color][num_neighborhoods] + cost[i][current_color - 1])
                            else:
                                dp[i][current_color][num_neighborhoods] = min(
                                    dp[i][current_color][num_neighborhoods],
                                    dp[i - 1][prev_color][num_neighborhoods - 1] + cost[i][current_color - 1])
            else:
                color = houses[i]
                for num_neighborhoods in range(1, min(target, i + 1) + 1):
                    for prev_color in range(1, n + 1):
                        if color == prev_color:
                            dp[i][color][num_neighborhoods] = min(
                                dp[i][color][num_neighborhoods],
                                dp[i - 1][color][num_neighborhoods])
                        else:
                            dp[i][color][num_neighborhoods] = min(
                                dp[i][color][num_neighborhoods],
                                dp[i - 1][prev_color][num_neighborhoods - 1])
        minimal_cost = min(dp[m - 1][color][target] for color in range(1, n + 1))
        return -1 if minimal_cost >= LARGE_NUMBER else minimal_cost

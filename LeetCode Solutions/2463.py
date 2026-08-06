class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        n, m = len(robot), len(factory)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 0

        for i in range(1, m + 1):
            pos, limit = factory[i - 1]
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]

                dist = 0
                for k in range(1, min(limit, j) + 1):
                    dist += abs(robot[j - k] - pos)
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + dist)

        return dp[m][n]
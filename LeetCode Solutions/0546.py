class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * (n + 1) for _ in range(n)] for _ in range(n)]
        def dfs(i, j, k):
            if i > j:
                return 0
            if dp[i][j][k] > 0:
                return dp[i][j][k]
            max_points = (k + 1) * (k + 1) + dfs(i + 1, j, 0)
            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    max_points = max(max_points, dfs(i + 1, m - 1, 0) + dfs(m, j, k + 1))
            dp[i][j][k] = max_points
            return max_points
        return dfs(0, n - 1, 0)

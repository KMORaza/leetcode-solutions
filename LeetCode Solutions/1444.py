from typing import List
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        X = 1000000007
        m, n = len(pizza), len(pizza[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prefix_sum[i][j] = (prefix_sum[i + 1][j] + prefix_sum[i][j + 1]
                                    - prefix_sum[i + 1][j + 1] + (pizza[i][j] == 'A'))
        def has_apple(x1, y1, x2, y2) -> bool:
            return (prefix_sum[x1][y1] - prefix_sum[x2][y1] - prefix_sum[x1][y2] + prefix_sum[x2][y2]) > 0
        dp = [[[None] * k for _ in range(n)] for _ in range(m)]
        def count_ways(x, y, cuts_left):
            if cuts_left == 0:
                return 1 if has_apple(x, y, m, n) else 0
            if dp[x][y][cuts_left] is not None:
                return dp[x][y][cuts_left]
            result = 0
            for j in range(y + 1, n):
                if has_apple(x, y, m, j):
                    result = (result + count_ways(x, j, cuts_left - 1)) % X
            for i in range(x + 1, m):
                if has_apple(x, y, i, n):
                    result = (result + count_ways(i, y, cuts_left - 1)) % X
            dp[x][y][cuts_left] = result
            return result
        return count_ways(0, 0, k - 1)

class Solution:
    def mergeStones(self, stones: list[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        prefix_sums = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + stones[i - 1]
        infinity = 1 << 20
        dp_costs = [[[infinity] * (K + 1) for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp_costs[i][i][1] = 0
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                for piles in range(1, K + 1):
                    for mid in range(i, j):
                        dp_costs[i][j][piles] = min(dp_costs[i][j][piles],
                                                    dp_costs[i][mid][1] + dp_costs[mid + 1][j][piles - 1])
                dp_costs[i][j][1] = dp_costs[i][j][K] + prefix_sums[j] - prefix_sums[i - 1]
        return dp_costs[1][n][1]

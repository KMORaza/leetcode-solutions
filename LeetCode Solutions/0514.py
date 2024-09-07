from collections import defaultdict, deque
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        position_map = defaultdict(list)
        for i, char in enumerate(ring):
            position_map[char].append(i)
        m, n = len(ring), len(key)
        dp = [[float('inf')] * m for _ in range(n)]
        for pos in position_map[key[0]]:
            dp[0][pos] = min(pos, m - pos) + 1
        for i in range(1, n):
            for j in range(m):
                if dp[i-1][j] == float('inf'):
                    continue
                for k in position_map[key[i]]:
                    diff = abs(j - k)
                    dp[i][k] = min(dp[i][k], dp[i-1][j] + min(diff, m - diff) + 1)
        return min(dp[n-1])

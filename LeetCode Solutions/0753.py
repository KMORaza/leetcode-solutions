class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        from collections import deque
        visited = set()
        mod = 10**(n - 1)
        result = []
        def dfs(u: int):
            for x in range(k):
                combo = u * 10 + x
                if combo not in visited:
                    visited.add(combo)
                    dfs(combo % mod)
                    result.append(str(x))
        dfs(0)
        result.append('0' * (n - 1))
        return ''.join(result)

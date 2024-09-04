class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        def dfs(x: str, y: str) -> bool:
            if (x, y) in memo:
                return memo[(x, y)]
            if x == y:
                memo[(x, y)] = True
                return True
            if sorted(x) != sorted(y):
                memo[(x, y)] = False
                return False
            n = len(x)
            for i in range(1, n):
                if (dfs(x[:i], y[:i]) and dfs(x[i:], y[i:])) or (dfs(x[:i], y[-i:]) and dfs(x[i:], y[:-i])):
                    memo[(x, y)] = True
                    return True
            memo[(x, y)] = False
            return False
        return dfs(s1, s2)
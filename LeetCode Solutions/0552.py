class Solution:
    def checkRecord(self, n: int) -> int:
        mod = int(1e9 + 7)
        self.n = n
        self.f = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
        return self.dfs(0, 0, 0, mod)
    def dfs(self, i: int, j: int, k: int, mod: int) -> int:
        if i >= self.n:
            return 1
        if self.f[i][j][k] != -1:
            return self.f[i][j][k]
        ans = self.dfs(i + 1, j, 0, mod)
        if j == 0:
            ans = (ans + self.dfs(i + 1, j + 1, 0, mod)) % mod
        if k < 2:
            ans = (ans + self.dfs(i + 1, j, k + 1, mod)) % mod
        self.f[i][j][k] = ans
        return ans

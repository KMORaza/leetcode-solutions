class Solution:
    def superEggDrop(self, x: int, n: int) -> int:
        memoization = [[-1] * (n + 1) for _ in range(x + 1)]
        return self.drop(x, n, memoization)
    def drop(self, x: int, n: int, memoization: list[list[int]]) -> int:
        if x == 0:
            return 0
        if x == 1:
            return n
        if n == 0:
            return 0
        if n == 1:
            return 1
        if memoization[x][n] != -1:
            return memoization[x][n]
        l, r = 1, n + 1
        while l < r:
            m = (l + r) // 2
            broken = self.drop(x - 1, m - 1, memoization)
            unbroken = self.drop(x, n - m, memoization)
            if broken >= unbroken:
                r = m
            else:
                l = m + 1
        memoization[x][n] = 1 + self.drop(x - 1, l - 1, memoization)
        return memoization[x][n]

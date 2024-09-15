class Solution:
    def minDeletionSize(self, st):
        k = len(st[0])
        dp = [1] * k
        for i in range(1, k):
            for j in range(i):
                if self.sorted(st, j, i):
                    dp[i] = max(dp[i], dp[j] + 1)
        return k - max(dp)
    def sorted(self, st, j, i):
        for s in st:
            if s[j] > s[i]:
                return False
        return True

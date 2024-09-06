class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        m, n = len(s1), len(s2)
        d = [[0, 0] for _ in range(n)]
        for i in range(n):
            j = i
            cnt = 0
            for k in range(m):
                if s1[k] == s2[j]:
                    j += 1
                    if j == n:
                        j = 0
                        cnt += 1
            d[i] = [cnt, j]

        ans = 0
        j = 0
        while n1 > 0:
            ans += d[j][0]
            j = d[j][1]
            n1 -= 1
        return ans // n2
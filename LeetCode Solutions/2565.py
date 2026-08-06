from typing import List

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        left = [-1] * m
        j = 0
        for i in range(n):
            if j < m and s[i] == t[j]:
                left[j] = i
                j += 1

        right = [-1] * m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and s[i] == t[j]:
                right[j] = i
                j -= 1

        def check(k):
            for l in range(m - k + 1):
                r = l + k

                if l == 0:
                    if r == m or right[r] != -1:
                        return True
                elif r == m:
                    if left[l - 1] != -1:
                        return True
                elif left[l - 1] != -1 and right[r] != -1 and left[l - 1] < right[r]:
                    return True

            return False

        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
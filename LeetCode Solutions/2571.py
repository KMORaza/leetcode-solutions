class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0

        while n:
            if n & 1 == 0:
                n >>= 1
            else:
                ans += 1
                if n == 3 or (n & 3) == 1:
                    n -= 1
                else:
                    n += 1

        return ans
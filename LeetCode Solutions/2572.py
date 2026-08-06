from typing import List
from collections import Counter

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def get_mask(x):
            mask = 0

            for i, p in enumerate(primes):
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1

                if cnt > 1:
                    return -1

                if cnt:
                    mask |= 1 << i

            return mask

        freq = Counter(nums)

        dp = [0] * (1 << 10)
        dp[0] = 1

        for x, cnt in freq.items():
            if x == 1:
                continue

            mask = get_mask(x)

            if mask == -1:
                continue

            ndp = dp[:]

            for state in range(1 << 10):
                if state & mask == 0:
                    ndp[state | mask] = (ndp[state | mask] + dp[state] * cnt) % MOD

            dp = ndp

        ans = sum(dp) % MOD
        ans = ans * pow(2, freq[1], MOD) % MOD

        return (ans - 1) % MOD
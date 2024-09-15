from itertools import combinations
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        from math import inf
        n = len(nums)
        subset_len = n // k
        comp = [-1] * (1 << n)
        for i in range(1, 1 << n):
            if bin(i).count('1') != subset_len:
                continue
            elems = set()
            min_val = 20
            max_val = 0
            for j in range(n):
                if (i >> j) & 1:
                    if nums[j] in elems:
                        break
                    elems.add(nums[j])
                    min_val = min(min_val, nums[j])
                    max_val = max(max_val, nums[j])
            if len(elems) == subset_len:
                comp[i] = max_val - min_val
        dp = [inf] * (1 << n)
        dp[0] = 0
        for i in range(1 << n):
            if dp[i] == inf:
                continue
            used = set()
            mask = 0
            for j in range(n):
                if (i >> j) & 1 == 0 and nums[j] not in used:
                    used.add(nums[j])
                    mask |= 1 << j
            if len(used) < subset_len:
                continue
            for j in range(mask, 0, -1):
                if (j & mask) == j and comp[j] != -1:
                    dp[i | j] = min(dp[i | j], dp[i] + comp[j])
        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != inf else -1
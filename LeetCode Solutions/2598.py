class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        from collections import Counter

        mod_counts = Counter()
        for num in nums:
            mod_counts[num % value] += 1

        mex = 0
        while True:
            mod_val = mex % value
            if mod_counts[mod_val] == 0:
                return mex
            mod_counts[mod_val] -= 1
            mex += 1

        return mex
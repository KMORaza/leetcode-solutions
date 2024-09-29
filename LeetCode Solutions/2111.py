from typing import List
import bisect
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def longest_non_decreasing_subsequence(seq):
            dp = []
            for x in seq:
                pos = bisect.bisect_right(dp, x)
                if pos == len(dp):
                    dp.append(x)
                else:
                    dp[pos] = x
            return len(dp)
        n = len(arr)
        total_removals = 0
        for start in range(k):
            subsequence = arr[start:n:k]
            lnds_length = longest_non_decreasing_subsequence(subsequence)
            total_removals += len(subsequence) - lnds_length
        return total_removals
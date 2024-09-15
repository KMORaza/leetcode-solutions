from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_len = 0
        for j in range(1, n):
            for i in range(j):
                k = index.get(arr[j] - arr[i], -1)
                if k != -1 and k < i:
                    dp[i, j] = dp.get((k, i), 2) + 1
                else:
                    dp[i, j] = 2
                max_len = max(max_len, dp[i, j])
        return max_len if max_len > 2 else 0

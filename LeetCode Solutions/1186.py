from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        dp = [0] * n
        dp_delete = [0] * n
        dp[0] = arr[0]
        dp_delete[0] = float('-inf')
        max_sum = arr[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
            dp_delete[i] = max(dp_delete[i-1] + arr[i], dp[i-1])
            max_sum = max(max_sum, dp[i], dp_delete[i])
        return max_sum

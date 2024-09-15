from typing import List
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n
        def dfs(index: int) -> int:
            if dp[index] != -1:
                return dp[index]
            max_jumps = 1
            for i in range(index - 1, max(index - d - 1, -1), -1):
                if arr[i] < arr[index]:
                    max_jumps = max(max_jumps, 1 + dfs(i))
                else:
                    break
            for i in range(index + 1, min(index + d + 1, n)):
                if arr[i] < arr[index]:
                    max_jumps = max(max_jumps, 1 + dfs(i))
                else:
                    break
            dp[index] = max_jumps
            return dp[index]
        result = 0
        for i in range(n):
            result = max(result, dfs(i))
        return result

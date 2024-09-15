from typing import List
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [None] * (target + 1)
        dp[0] = ''
        for i in range(1, target + 1):
            for digit in range(9, 0, -1):
                if i >= cost[digit - 1] and dp[i - cost[digit - 1]] is not None:
                    new_number = dp[i - cost[digit - 1]] + str(digit)
                    if dp[i] is None or len(new_number) > len(dp[i]) or (len(new_number) == len(dp[i]) and new_number > dp[i]):
                        dp[i] = new_number
        return dp[target] if dp[target] is not None else "0"


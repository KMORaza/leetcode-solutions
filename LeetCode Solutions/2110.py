from typing import List
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total_periods = len(prices)
        current_length = 0
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                current_length += 1
                total_periods += current_length
            else:
                current_length = 0
        return total_periods
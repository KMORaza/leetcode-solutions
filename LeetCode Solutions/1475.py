from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = prices[:]
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] -= prices[i]
            stack.append(i)
        return result

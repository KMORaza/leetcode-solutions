class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        min_price1 = float('inf')
        min_price2 = float('inf')
        profit1 = 0
        profit2 = 0
        for price in prices:
            min_price1 = min(min_price1, price)
            profit1 = max(profit1, price - min_price1)
            min_price2 = min(min_price2, price - profit1)
            profit2 = max(profit2, price - min_price2)
        return profit2

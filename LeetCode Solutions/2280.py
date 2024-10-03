from typing import List
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        if len(stockPrices) < 2:
            return 0
        lines = 0
        n = len(stockPrices)
        for i in range(1, n - 1):
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]
            x3, y3 = stockPrices[i + 1]
            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                lines += 1
        return lines + 1
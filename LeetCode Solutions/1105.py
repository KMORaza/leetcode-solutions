from typing import List
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            width_sum = 0
            max_height = 0
            for j in range(i, 0, -1):
                width_sum += books[j - 1][0]
                if width_sum > shelfWidth:
                    break
                max_height = max(max_height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + max_height)
        return dp[n]

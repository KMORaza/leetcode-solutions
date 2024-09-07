from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        candies_to_eat = n // 2
        unique_candies = len(set(candyType))
        return min(unique_candies, candies_to_eat)

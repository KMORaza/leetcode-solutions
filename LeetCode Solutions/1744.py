from typing import List
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix_sum = [0] * (len(candiesCount) + 1)
        for i in range(1, len(candiesCount) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + candiesCount[i - 1]
        result = []
        for type, day, cap in queries:
            min_candies = day + 1
            max_candies = cap * (day + 1)
            total_candies = prefix_sum[type + 1]
            if min_candies <= total_candies and max_candies > prefix_sum[type]:
                result.append(True)
            else:
                result.append(False)
        return result

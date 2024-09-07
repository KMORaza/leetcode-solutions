from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {restaurant: i for i, restaurant in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                i = index_map[restaurant]
                index_sum = i + j
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [restaurant]
                elif index_sum == min_sum:
                    result.append(restaurant)
        return result

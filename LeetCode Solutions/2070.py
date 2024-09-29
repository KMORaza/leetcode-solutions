from typing import List
import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        max_beauty = []
        current_max = 0
        for price, beauty in items:
            current_max = max(current_max, beauty)
            max_beauty.append(current_max)
        result = []
        for query in queries:
            index = bisect.bisect_right(items, [query, float('inf')]) - 1
            if index >= 0:
                result.append(max_beauty[index])
            else:
                result.append(0)
        return result
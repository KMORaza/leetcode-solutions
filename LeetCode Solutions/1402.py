from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        max_satisfaction = 0
        current_sum = 0
        current_total = 0
        for s in satisfaction:
            current_sum += s
            current_total += current_sum
            max_satisfaction = max(max_satisfaction, current_total)
        return max_satisfaction

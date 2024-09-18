from typing import List
class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) < 3:
            return 0.0
        total_sum = sum(salary)
        min_salary = min(salary)
        max_salary = max(salary)
        adjusted_sum = total_sum - min_salary - max_salary
        adjusted_count = len(salary) - 2
        return adjusted_sum / adjusted_count

from typing import List
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = 0
        max_val = 0
        current_sum = 0
        for diff in differences:
            current_sum += diff
            min_val = min(min_val, current_sum)
            max_val = max(max_val, current_sum)
        total_range = upper - lower + 1
        required_range = max_val - min_val + 1
        valid_starting_points = total_range - required_range + 1
        return max(0, valid_starting_points)
from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        non_covered_count = 0
        current_end = 0
        for start, end in intervals:
            if end > current_end:
                non_covered_count += 1
                current_end = end
        return non_covered_count

from bisect import bisect_left
class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        indexed_intervals = [(start, end, i) for i, (start, end) in enumerate(intervals)]
        indexed_intervals.sort(key=lambda x: x[0])
        start_times = [interval[0] for interval in indexed_intervals]
        result = [-1] * len(intervals)
        for start, end, original_index in indexed_intervals:
            pos = bisect_left(start_times, end)
            if pos < len(start_times):
                result[original_index] = indexed_intervals[pos][2]
        return result
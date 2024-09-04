class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = []
        current_interval = intervals[0]
        for interval in intervals[1:]:
            if current_interval[1] >= interval[0]:
                current_interval[1] = max(current_interval[1], interval[1])
            else:
                merged.append(current_interval)
                current_interval = interval
        merged.append(current_interval)
        return merged

from sortedcontainers import SortedDict
class MyCalendarThree:
    def __init__(self):
        self.time_points = SortedDict()
    def book(self, startTime: int, endTime: int) -> int:
        if startTime in self.time_points:
            self.time_points[startTime] += 1
        else:
            self.time_points[startTime] = 1
        if endTime in self.time_points:
            self.time_points[endTime] -= 1
        else:
            self.time_points[endTime] = -1
        current_overlap = 0
        max_overlap = 0
        for time, count in self.time_points.items():
            current_overlap += count
            max_overlap = max(max_overlap, current_overlap)
        return max_overlap

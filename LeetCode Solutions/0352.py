class SummaryRanges:
    def __init__(self):
        self.nums = set()
        self.intervals = []
    def addNum(self, value: int) -> None:
        if value in self.nums:
            return
        self.nums.add(value)
        new_intervals = []
        merged = False
        for start, end in self.intervals:
            if value < start - 1:
                new_intervals.append((start, end))
            elif value > end + 1:
                new_intervals.append((start, end))
            else:
                start = min(start, value)
                end = max(end, value)
                new_intervals.append((start, end))
                merged = True
        if not merged:
            new_intervals.append((value, value))
        merged_intervals = []
        for start, end in sorted(new_intervals):
            if merged_intervals and merged_intervals[-1][1] >= start - 1:
                merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], end))
            else:
                merged_intervals.append((start, end))
        self.intervals = merged_intervals
    def getIntervals(self) -> list:
        return self.intervals

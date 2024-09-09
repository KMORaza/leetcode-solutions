class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        n = len(self.intervals)
        while i < n and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i += 1
        while i < n and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1
        new_intervals.append([left, right])
        while i < n:
            new_intervals.append(self.intervals[i])
            i += 1
        self.intervals = new_intervals

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        n = len(self.intervals)
        while i < n:
            curr_left, curr_right = self.intervals[i]

            if curr_right <= left or curr_left >= right:
                new_intervals.append(self.intervals[i])
            else:
                if curr_left < left:
                    new_intervals.append([curr_left, left])
                if curr_right > right:
                    new_intervals.append([right, curr_right])
            i += 1
        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        i = 0
        n = len(self.intervals)
        while i < n and self.intervals[i][1] <= left:
            i += 1
        if i < n and self.intervals[i][0] <= left and self.intervals[i][1] >= right:
            return True
        return False

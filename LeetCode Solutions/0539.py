class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
        minutes.sort()
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        min_diff = min(min_diff, (1440 - minutes[-1]) + minutes[0])
        return min_diff

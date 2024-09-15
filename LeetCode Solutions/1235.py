from bisect import bisect_right
class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * n
        dp[0] = jobs[0][2]
        def find_last_non_overlapping(i):
            lo, hi = 0, i - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi
        for i in range(1, n):
            last_non_overlapping_index = find_last_non_overlapping(i)
            include_profit = jobs[i][2]
            if last_non_overlapping_index != -1:
                include_profit += dp[last_non_overlapping_index]
            dp[i] = max(dp[i - 1], include_profit)
        return dp[-1]

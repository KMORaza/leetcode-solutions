import bisect
class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in envelopes]
        dp = []
        for h in heights:
            index = bisect.bisect_left(dp, h)
            if index == len(dp):
                dp.append(h)
            else:
                dp[index] = h
        return len(dp)
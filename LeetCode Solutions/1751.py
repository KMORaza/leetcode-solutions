class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        dp = [[None] * (k + 1) for _ in range(len(events))]
        events.sort(key=lambda x: (x[0], x[1]))
        return self._helper(events, 0, k, dp)
    def _helper(self, events: List[List[int]], index: int, remaining: int, dp: List[List[int]]) -> int:
        if remaining == 0 or index == len(events):
            return 0
        if dp[index][remaining] is not None:
            return dp[index][remaining]
        next_index = self._findNext(events, index + 1, events[index][1] + 1)
        dp[index][remaining] = max(events[index][2] + self._helper(events, next_index, remaining - 1, dp),
                                   self._helper(events, index + 1, remaining, dp))
        return dp[index][remaining]
    def _findNext(self, events: List[List[int]], left: int, target: int) -> int:
        right = len(events)
        while left < right:
            mid = (left + right) // 2
            if events[mid][0] >= target:
                right = mid
            else:
                left = mid + 1
        return left

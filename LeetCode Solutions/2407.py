class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        from collections import defaultdict
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))

        events.sort()
        active = 0
        max_groups = 0
        for time, delta in events:
            active += delta
            max_groups = max(max_groups, active)

        return max_groups
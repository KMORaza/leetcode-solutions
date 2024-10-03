from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = []
        for start, end in flowers:
            events.append((start, 1))
            events.append((end + 1, -1))
        events.sort()
        result = []
        bloom_count = 0
        event_idx = 0
        sorted_people = sorted((time, idx) for idx, time in enumerate(people))
        blooms_at_time = [0] * len(people)
        for time, original_index in sorted_people:
            while event_idx < len(events) and events[event_idx][0] <= time:
                bloom_count += events[event_idx][1]
                event_idx += 1
            blooms_at_time[original_index] = bloom_count
        return blooms_at_time
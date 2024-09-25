from typing import List
import collections
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        events = []
        for start, end, color in segments:
            events.append((start, color))
            events.append((end, -color))
        events.sort()
        result = []
        current_color = 0
        last_position = events[0][0]
        for position, color_change in events:
            if current_color > 0 and position > last_position:
                result.append([last_position, position, current_color])
            current_color += color_change
            last_position = position
        return result

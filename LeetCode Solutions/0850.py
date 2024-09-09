from typing import List, Tuple
from collections import namedtuple
RectangleEvent = namedtuple('RectangleEvent', ['x', 'y1', 'y2', 'type'])
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 1_000_000_007
        events = []
        for r in rectangles:
            events.append(RectangleEvent(r[0], r[1], r[3], 's'))
            events.append(RectangleEvent(r[2], r[1], r[3], 'e'))
        events.sort(key=lambda e: e.x)
        output = 0
        previous_x = 0
        y_pairs = []
        for e in events:
            if e.x > previous_x:
                width = e.x - previous_x
                output = (output + width * self.getTotalHeight(y_pairs)) % MOD
                previous_x = e.x
            if e.type == 's':
                y_pairs.append((e.y1, e.y2))
                y_pairs.sort(key=lambda pair: pair[0])
            else:
                y_pairs.remove((e.y1, e.y2))
        return int(output % MOD)
    def getTotalHeight(self, y_pairs: List[Tuple[int, int]]) -> int:
        total_height = 0
        previous_y = 0
        for y1, y2 in y_pairs:
            previous_y = max(previous_y, y1)
            if y2 > previous_y:
                total_height += y2 - previous_y
                previous_y = y2
        return total_height

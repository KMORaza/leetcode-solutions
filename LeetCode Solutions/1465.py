from typing import List
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_horizontal_gap = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_horizontal_gap = max(max_horizontal_gap, horizontalCuts[i] - horizontalCuts[i - 1])
        max_vertical_gap = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_vertical_gap = max(max_vertical_gap, verticalCuts[i] - verticalCuts[i - 1])
        return (max_horizontal_gap * max_vertical_gap) % (10**9 + 7)

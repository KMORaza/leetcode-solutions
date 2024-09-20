from collections import deque
class Solution:
    def maximumScore(self, heights: list[int], index: int) -> int:
        max_area = 0
        height_stack = deque()
        heights.append(0)
        for position in range(len(heights)):
            while height_stack and (position == len(heights) or heights[height_stack[-1]] > heights[position]):
                current_height = heights[height_stack.pop()]
                current_width = position if not height_stack else position - height_stack[-1] - 1
                if (not height_stack or height_stack[-1] + 1 <= index) and position - 1 >= index:
                    max_area = max(max_area, current_height * current_width)
            height_stack.append(position)
        return max_area

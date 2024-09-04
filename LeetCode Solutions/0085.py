class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        matrix = [[int(matrix[i][j]) for j in range(cols)] for i in range(rows)]
        heights = [0] * cols
        max_area = 0
        for row in matrix:
            # Update heights
            for j in range(cols):
                if row[j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        index = 0
        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (heights[top_of_stack] *
                       ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)
        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                   ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
        return max_area
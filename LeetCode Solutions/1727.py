class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        max_area = 0
        if not matrix or not matrix[0]:
            return max_area
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] else 0
            sorted_heights = sorted(heights, reverse=True)
            for j in range(cols):
                max_area = max(max_area, sorted_heights[j] * (j + 1))
        return max_area

from typing import List
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def countOverlap(offsetX: int, offsetY: int) -> int:
            count = 0
            for i in range(n):
                for j in range(n):
                    x, y = i + offsetX, j + offsetY
                    if 0 <= x < n and 0 <= y < n and img1[i][j] == 1 and img2[x][y] == 1:
                        count += 1
            return count
        n = len(img1)
        max_overlap = 0
        for x_shift in range(-n + 1, n):
            for y_shift in range(-n + 1, n):
                max_overlap = max(max_overlap, countOverlap(x_shift, y_shift))
        return max_overlap

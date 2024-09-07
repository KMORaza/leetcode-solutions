from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if not img:
            return []
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                total_sum = 0
                count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        total_sum += img[ni][nj]
                        count += 1
                result[i][j] = total_sum // count
        return result

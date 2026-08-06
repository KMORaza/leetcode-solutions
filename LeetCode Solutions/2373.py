class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                max_val = 0
                for di in range(3):
                    for dj in range(3):
                        max_val = max(max_val, grid[i + di][j + dj])
                result[i][j] = max_val

        return result
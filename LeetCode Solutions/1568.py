class Solution:
    def minDays(self, matrix):
        if self.isSevered(matrix):
            return 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    matrix[row][col] = 0
                    if self.isSevered(matrix):
                        return 1
                    matrix[row][col] = 1
        return 2
    def isSevered(self, matrix):
        numIslands = 0
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0 or visited[row][col]:
                    continue
                if numIslands + 1 > 1:
                    return True
                numIslands += 1
                self.explore(matrix, row, col, visited)
        return numIslands != 1
    def explore(self, matrix, row, col, visited):
        visited[row][col] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            newRow, newCol = row + dx, col + dy
            if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]) and matrix[newRow][newCol] == 1 and not visited[newRow][newCol]:
                self.explore(matrix, newRow, newCol, visited)

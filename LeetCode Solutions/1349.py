class Solution:
    def maxStudents(self, grid: list[list[str]]) -> int:
        def findMaxPairs(grid):
            rows, cols = len(grid), len(grid[0])
            total_pairs = 0
            visited = [[-1] * cols for _ in range(rows)]
            pair_match = [[-1] * cols for _ in range(rows)]
            def search(x, y, session_tag):
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == '.' and visited[new_x][new_y] != session_tag:
                        visited[new_x][new_y] = session_tag
                        if pair_match[new_x][new_y] == -1 or search(pair_match[new_x][new_y] // cols, pair_match[new_x][new_y] % cols, session_tag):
                            pair_match[new_x][new_y] = x * cols + y
                            pair_match[x][y] = new_x * cols + new_y
                            return True
                return False
            directions = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == '.' and pair_match[row][col] == -1:
                        current_session = row * cols + col
                        visited[row][col] = current_session
                        if search(row, col, current_session):
                            total_pairs += 1
            return total_pairs
        total_empty = sum(cell == '.' for row in grid for cell in row)
        return total_empty - findMaxPairs(grid)

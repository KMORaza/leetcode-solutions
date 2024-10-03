class Solution:
    def countUnguarded(self, height: int, width: int, sentinels: list[list[int]], obstacles: list[list[int]]) -> int:
        grid_map = [[0] * width for _ in range(height)]
        for sentinel in sentinels:
            grid_map[sentinel[0]][sentinel[1]] = 2
        for obstacle in obstacles:
            grid_map[obstacle[0]][obstacle[1]] = 2
        movement_vectors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for sentinel in sentinels:
            start_row, start_col = sentinel
            for row_change, col_change in movement_vectors:
                current_row, current_col = start_row, start_col
                while 0 <= current_row + row_change < height and 0 <= current_col + col_change < width and grid_map[current_row + row_change][current_col + col_change] < 2:
                    current_row += row_change
                    current_col += col_change
                    grid_map[current_row][current_col] = 1
        unguarded_cells = sum(cell == 0 for row in grid_map for cell in row)
        return unguarded_cells
from collections import deque
from typing import List
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        movement_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_rows, total_cols = len(grid), len(grid[0])
        min_price, max_price = pricing[0], pricing[1]
        initial_row, initial_col = start[0], start[1]
        output_list = []
        if min_price <= grid[initial_row][initial_col] <= max_price:
            output_list.append([initial_row, initial_col])
            if k == 1:
                return output_list
        position_queue = deque([(initial_row, initial_col)])
        visited_cells = [[False] * total_cols for _ in range(total_rows)]
        visited_cells[initial_row][initial_col] = True
        while position_queue:
            adjacent_cells = []
            for _ in range(len(position_queue)):
                current_r, current_c = position_queue.popleft()
                for delta_x, delta_y in movement_directions:
                    next_r, next_c = current_r + delta_x, current_c + delta_y
                    if 0 <= next_r < total_rows and 0 <= next_c < total_cols and grid[next_r][next_c] != 0 and not visited_cells[next_r][next_c]:
                        if min_price <= grid[next_r][next_c] <= max_price:
                            adjacent_cells.append([next_r, next_c])
                        position_queue.append((next_r, next_c))
                        visited_cells[next_r][next_c] = True
            adjacent_cells.sort(key=lambda cell: (grid[cell[0]][cell[1]], cell[0], cell[1]))
            for cell in adjacent_cells:
                if len(output_list) < k:
                    output_list.append(cell)
                if len(output_list) == k:
                    return output_list
        return output_list

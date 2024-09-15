from collections import deque
class Solution:
    def minCost(self, matrix):
        rows_count = len(matrix)
        cols_count = len(matrix[0])
        visited_cells = [[False] * cols_count for _ in range(rows_count)]
        BFS_queue = deque([(0, 0, 0)])
        movement_directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        while BFS_queue:
            current_row, current_col, current_cost = BFS_queue.popleft()
            if current_row == rows_count - 1 and current_col == cols_count - 1:
                return current_cost
            if visited_cells[current_row][current_col]:
                continue
            visited_cells[current_row][current_col] = True
            for direction_index in range(1, 5):
                next_row = current_row + movement_directions[direction_index][0]
                next_col = current_col + movement_directions[direction_index][1]
                if 0 <= next_row < rows_count and 0 <= next_col < cols_count:
                    if matrix[current_row][current_col] == direction_index:
                        BFS_queue.appendleft((next_row, next_col, current_cost))
                    else:
                        BFS_queue.append((next_row, next_col, current_cost + 1))
        return -1

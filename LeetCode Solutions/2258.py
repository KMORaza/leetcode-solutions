from collections import deque
class Solution:
    def maximumMinutes(self, grid):
        movement_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_cells = len(grid) * len(grid[0])
        fire_arrival_time = [[-1] * len(grid[0]) for _ in range(len(grid))]
        self.calculateFireArrival(grid, fire_arrival_time, movement_directions)
        max_time = -1
        start_time, end_time = 0, total_cells
        while start_time <= end_time:
            mid_time = (start_time + end_time) // 2
            if self.isPathAvailable(grid, fire_arrival_time, mid_time, movement_directions):
                max_time = mid_time
                start_time = mid_time + 1
            else:
                end_time = mid_time - 1
        return int(1e9) if max_time == total_cells else max_time
    def calculateFireArrival(self, grid, fire_arrival_time, movement_directions):
        elapsed_time = 0
        fire_queue = deque()
        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                if grid[row_index][col_index] == 1:
                    fire_queue.append((row_index, col_index))
                    fire_arrival_time[row_index][col_index] = 0
        while fire_queue:
            elapsed_time += 1
            for _ in range(len(fire_queue)):
                current_row, current_col = fire_queue.popleft()
                for dx, dy in movement_directions:
                    new_row, new_col = current_row + dx, current_col + dy
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        if grid[new_row][new_col] == 2:
                            continue
                        if fire_arrival_time[new_row][new_col] != -1:
                            continue
                        fire_arrival_time[new_row][new_col] = elapsed_time
                        fire_queue.append((new_row, new_col))
    def isPathAvailable(self, grid, fire_arrival_time, time_limit, movement_directions):
        path_queue = deque([(0, 0)])
        visited_cells = [[False] * len(grid[0]) for _ in range(len(grid))]
        visited_cells[0][0] = True
        while path_queue:
            time_limit += 1
            for _ in range(len(path_queue)):
                current_row, current_col = path_queue.popleft()
                for dx, dy in movement_directions:
                    new_row, new_col = current_row + dx, current_col + dy
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        if grid[new_row][new_col] == 2:
                            continue
                        if new_row == len(grid) - 1 and new_col == len(grid[0]) - 1:
                            if fire_arrival_time[new_row][new_col] != -1 and fire_arrival_time[new_row][new_col] < time_limit:
                                continue
                            return True
                        if fire_arrival_time[new_row][new_col] != -1 and fire_arrival_time[new_row][new_col] <= time_limit:
                            continue
                        if visited_cells[new_row][new_col]:
                            continue
                        path_queue.append((new_row, new_col))
                        visited_cells[new_row][new_col] = True
        return False

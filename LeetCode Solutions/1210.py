class Solution:
    def __init__(self):
        self.grid_size = 0
        self.grid = []
        self.visited_states = []
        self.bfs_queue = deque()
    def minimumMoves(self, grid):
        self.grid = grid
        self.grid_size = len(grid)
        self.visited_states = [[False] * 2 for _ in range(self.grid_size * self.grid_size)]
        target_position = (self.grid_size * self.grid_size - 2, self.grid_size * self.grid_size - 1)
        self.bfs_queue.append((0, 1))
        self.visited_states[0][0] = True
        steps_count = 0
        while self.bfs_queue:
            level_size = len(self.bfs_queue)
            for _ in range(level_size):
                head, tail = self.bfs_queue.popleft()
                if (head, tail) == target_position:
                    return steps_count
                head_row = head // self.grid_size
                head_col = head % self.grid_size
                tail_row = tail // self.grid_size
                tail_col = tail % self.grid_size
                self.try_move(head_row, head_col + 1, tail_row, tail_col + 1)
                self.try_move(head_row + 1, head_col, tail_row + 1, tail_col)
                if head_row == tail_row and head_row + 1 < self.grid_size and self.grid[head_row + 1][tail_col] == 0:
                    self.try_move(head_row, head_col, head_row + 1, head_col)
                if head_col == tail_col and head_col + 1 < self.grid_size and self.grid[tail_row][head_col + 1] == 0:
                    self.try_move(head_row, head_col, head_row, head_col + 1)
            steps_count += 1
        return -1
    def try_move(self, head_row, head_col, tail_row, tail_col):
        if (0 <= head_row < self.grid_size and 0 <= head_col < self.grid_size and
            0 <= tail_row < self.grid_size and 0 <= tail_col < self.grid_size):
            head_pos = head_row * self.grid_size + head_col
            tail_pos = tail_row * self.grid_size + tail_col
            orientation = 0 if head_row == tail_row else 1
            if not self.visited_states[head_pos][orientation] and self.grid[head_row][head_col] == 0 and self.grid[tail_row][tail_col] == 0:
                self.bfs_queue.append((head_pos, tail_pos))
                self.visited_states[head_pos][orientation] = True

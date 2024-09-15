class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def convert_to_flat_index(row: int, col: int) -> int:
            return row * num_cols + col
        def position_is_valid(row: int, col: int) -> bool:
            return 0 <= row < num_rows and 0 <= col < num_cols and grid[row][col] != "#"
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "S":
                    player_row, player_col = r, c
                elif cell == "B":
                    box_row, box_col = r, c
        num_rows, num_cols = len(grid), len(grid[0])
        direction_deltas = (-1, 0, 1, 0, -1)
        queue = deque([(convert_to_flat_index(player_row, player_col), convert_to_flat_index(box_row, box_col), 0)])
        visited = [[False] * (num_rows * num_cols) for _ in range(num_rows * num_cols)]
        visited[convert_to_flat_index(player_row, player_col)][convert_to_flat_index(box_row, box_col)] = True
        while queue:
            current_player, current_box, moves = queue.popleft()
            box_r, box_c = current_box // num_cols, current_box % num_cols
            if grid[box_r][box_c] == "T":
                return moves
            player_r, player_c = current_player // num_cols, current_player % num_cols
            for delta_row, delta_col in zip(direction_deltas, direction_deltas[1:]):
                new_player_r, new_player_c = player_r + delta_row, player_c + delta_col
                if not position_is_valid(new_player_r, new_player_c):
                    continue
                if new_player_r == box_r and new_player_c == box_c:
                    new_box_r, new_box_c = box_r + delta_row, box_c + delta_col
                    if not position_is_valid(new_box_r, new_box_c) or visited[convert_to_flat_index(new_player_r, new_player_c)][convert_to_flat_index(new_box_r, new_box_c)]:
                        continue
                    visited[convert_to_flat_index(new_player_r, new_player_c)][convert_to_flat_index(new_box_r, new_box_c)] = True
                    queue.append((convert_to_flat_index(new_player_r, new_player_c), convert_to_flat_index(new_box_r, new_box_c), moves + 1))
                elif not visited[convert_to_flat_index(new_player_r, new_player_c)][convert_to_flat_index(box_r, box_c)]:
                    visited[convert_to_flat_index(new_player_r, new_player_c)][convert_to_flat_index(box_r, box_c)] = True
                    queue.appendleft((convert_to_flat_index(new_player_r, new_player_c), convert_to_flat_index(box_r, box_c), moves))
        return -1

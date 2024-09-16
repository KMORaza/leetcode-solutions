from typing import List
from collections import deque
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def bfs(start_row: int, start_col: int) -> List[tuple]:
            component = set()
            border = set()
            queue = deque([(start_row, start_col)])
            original_color = grid[start_row][start_col]
            while queue:
                r, c = queue.popleft()
                if (r, c) in component:
                    continue
                component.add((r, c))
                is_border = False
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == original_color:
                            if (nr, nc) not in component:
                                queue.append((nr, nc))
                        else:
                            is_border = True
                    else:
                        is_border = True
                if is_border:
                    border.add((r, c))
            return component, border
        component, border = bfs(row, col)
        for r, c in border:
            grid[r][c] = color
        return grid

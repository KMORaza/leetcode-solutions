from typing import List
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        start = ''.join(str(num) for row in board for num in row)
        def is_solvable(board_str):
            one_d = [num for num in board_str if num != '0']
            inversions = 0
            for i in range(len(one_d)):
                for j in range(i + 1, len(one_d)):
                    if one_d[i] > one_d[j]:
                        inversions += 1
            return inversions % 2 == 0
        if not is_solvable(start):
            return -1
        def get_neighbors(state):
            neighbors = []
            zero_pos = state.index('0')
            row, col = divmod(zero_pos, 3)
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= r < 2 and 0 <= c < 3:
                    new_pos = r * 3 + c
                    new_state = list(state)
                    new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
                    neighbors.append(''.join(new_state))
            return neighbors
        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)
        while queue:
            current, moves = queue.popleft()
            if current == target:
                return moves
            for neighbor in get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, moves + 1))
        return -1

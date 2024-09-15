from collections import deque
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def to_string(matrix):
            return ''.join(''.join(map(str, row)) for row in matrix)
        def flip(matrix, r, c):
            directions = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
            new_matrix = [row[:] for row in matrix]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                    new_matrix[nr][nc] ^= 1
            return new_matrix
        rows, cols = len(mat), len(mat[0])
        initial_state = to_string(mat)
        target_state = '0' * (rows * cols)
        if initial_state == target_state:
            return 0
        queue = deque([(mat, 0)])
        visited = set()
        visited.add(initial_state)
        while queue:
            current_matrix, flips = queue.popleft()
            for r in range(rows):
                for c in range(cols):
                    new_matrix = flip(current_matrix, r, c)
                    new_state = to_string(new_matrix)
                    if new_state == target_state:
                        return flips + 1
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_matrix, flips + 1))
        return -1

import heapq
from typing import List
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        rows = len(mat)
        heap = []
        initial_sum = sum(row[0] for row in mat)
        initial_indices = tuple(0 for _ in range(rows))
        heapq.heappush(heap, (initial_sum, initial_indices))
        visited = set()
        visited.add(initial_indices)
        for _ in range(k):
            current_sum, indices = heapq.heappop(heap)
            if _ == k - 1:
                return current_sum
            for r in range(rows):
                if indices[r] + 1 < len(mat[r]):
                    new_indices = list(indices)
                    new_indices[r] += 1
                    new_indices = tuple(new_indices)
                    new_sum = current_sum - mat[r][indices[r]] + mat[r][new_indices[r]]
                    if new_indices not in visited:
                        visited.add(new_indices)
                        heapq.heappush(heap, (new_sum, new_indices))
        return -1

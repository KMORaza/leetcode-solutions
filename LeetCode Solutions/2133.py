from typing import List
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in matrix:
            if len(set(row)) != n:
                return False
        for col in range(n):
            seen = set()
            for row in range(n):
                seen.add(matrix[row][col])
            if len(seen) != n:
                return False
        return True
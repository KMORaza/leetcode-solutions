class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_rows = [min(row) for row in matrix]
        max_cols = [max(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))]
        return [num for num in min_rows if num in max_cols]

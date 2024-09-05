class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sums = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.prefix_sums[i][j] = (matrix[i-1][j-1] +
                                          self.prefix_sums[i-1][j] +
                                          self.prefix_sums[i][j-1] -
                                          self.prefix_sums[i-1][j-1])
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix_sums[row2 + 1][col2 + 1] -
                self.prefix_sums[row1][col2 + 1] -
                self.prefix_sums[row2 + 1][col1] +
                self.prefix_sums[row1][col1])

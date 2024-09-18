class Solution:
    def numSubmat(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        total_count = 0
        for start_row in range(rows):
            current_row = [1] * cols
            for row in range(start_row, rows):
                for col in range(cols):
                    current_row[col] &= matrix[row][col]
                total_count += self.calculate_submatrices(current_row)
        return total_count
    def calculate_submatrices(self, row):
        count = 0
        length = 0
        for value in row:
            if value == 0:
                length = 0
            else:
                length += 1
            count += length
        return count

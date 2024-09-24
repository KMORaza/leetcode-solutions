class Solution:
    def check_bounds(self, row_idx, col_idx, total_rows, total_cols):
        return 0 <= row_idx < total_rows and 0 <= col_idx < total_cols
    def getBiggestThree(self, data_matrix):
        sum_set = set()
        total_rows, total_cols = len(data_matrix), len(data_matrix[0])
        for r in range(total_rows):
            for c in range(total_cols):
                sum_set.add(data_matrix[r][c])
        for diamond_size in range(1, 51):
            for r in range(total_rows):
                for c in range(total_cols):
                    if (self.check_bounds(r - diamond_size, c, total_rows, total_cols) and
                        self.check_bounds(r, c - diamond_size, total_rows, total_cols) and
                        self.check_bounds(r + diamond_size, c, total_rows, total_cols) and
                        self.check_bounds(r, c + diamond_size, total_rows, total_cols)):
                        diamond_sum = (
                            data_matrix[r - diamond_size][c] +
                            data_matrix[r + diamond_size][c] +
                            data_matrix[r][c - diamond_size] +
                            data_matrix[r][c + diamond_size]
                        )
                        for offset in range(1, diamond_size):
                            diamond_sum += data_matrix[r - offset][c + diamond_size - offset]
                        for offset in range(1, diamond_size):
                            diamond_sum += data_matrix[r - offset][c - diamond_size + offset]
                        for offset in range(1, diamond_size):
                            diamond_sum += data_matrix[r + offset][c + diamond_size - offset]
                        for offset in range(1, diamond_size):
                            diamond_sum += data_matrix[r + offset][c - diamond_size + offset]
                        sum_set.add(diamond_sum)
        sorted_values = sorted(sum_set, reverse=True)
        return sorted_values[:3]

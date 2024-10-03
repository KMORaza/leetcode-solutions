class Solution:
    def maxTrailingZeros(self, grid):
        row_count = len(grid)
        col_count = len(grid[0])
        count2_left = [[0] * col_count for _ in range(row_count)]
        count5_left = [[0] * col_count for _ in range(row_count)]
        count2_top = [[0] * col_count for _ in range(row_count)]
        count5_top = [[0] * col_count for _ in range(row_count)]
        for r in range(row_count):
            for c in range(col_count):
                count2_left[r][c] = self.factorCount(grid[r][c], 2)
                count5_left[r][c] = self.factorCount(grid[r][c], 5)
                if c > 0:
                    count2_left[r][c] += count2_left[r][c - 1]
                    count5_left[r][c] += count5_left[r][c - 1]
        for c in range(col_count):
            for r in range(row_count):
                count2_top[r][c] = self.factorCount(grid[r][c], 2)
                count5_top[r][c] = self.factorCount(grid[r][c], 5)
                if r > 0:
                    count2_top[r][c] += count2_top[r - 1][c]
                    count5_top[r][c] += count5_top[r - 1][c]
        max_zeros = 0
        for r in range(row_count):
            for c in range(col_count):
                current_factor2 = self.factorCount(grid[r][c], 2)
                current_factor5 = self.factorCount(grid[r][c], 5)
                left_factor2 = count2_left[r][c]
                left_factor5 = count5_left[r][c]
                right_factor2 = count2_left[r][col_count - 1] - (count2_left[r][c - 1] if c > 0 else 0)
                right_factor5 = count5_left[r][col_count - 1] - (count5_left[r][c - 1] if c > 0 else 0)
                top_factor2 = count2_top[r][c]
                top_factor5 = count5_top[r][c]
                down_factor2 = count2_top[row_count - 1][c] - (count2_top[r - 1][c] if r > 0 else 0)
                down_factor5 = count5_top[row_count - 1][c] - (count5_top[r - 1][c] if r > 0 else 0)
                max_zeros = max(max_zeros, max(
                    min(left_factor2 + top_factor2 - current_factor2, left_factor5 + top_factor5 - current_factor5),
                    min(right_factor2 + top_factor2 - current_factor2, right_factor5 + top_factor5 - current_factor5),
                    min(left_factor2 + down_factor2 - current_factor2, left_factor5 + down_factor5 - current_factor5),
                    min(right_factor2 + down_factor2 - current_factor2, right_factor5 + down_factor5 - current_factor5)
                ))
        return max_zeros
    def factorCount(self, number, divisor):
        total_count = 0
        while number % divisor == 0:
            number //= divisor
            total_count += 1
        return total_count

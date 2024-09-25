class Solution:
    def rotateGrid(self, matrix, num_rotations):
        height = len(matrix)
        width = len(matrix[0])
        upper_bound, left_bound, lower_bound, right_bound = 0, 0, height - 1, width - 1
        while upper_bound < lower_bound and left_bound < right_bound:
            perimeter_count = 2 * (lower_bound - upper_bound + 1) + 2 * (right_bound - left_bound + 1) - 4
            effective_rotations = num_rotations % perimeter_count
            for _ in range(effective_rotations):
                initial_element = matrix[upper_bound][left_bound]
                for col in range(left_bound, right_bound):
                    matrix[upper_bound][col] = matrix[upper_bound][col + 1]
                for row in range(upper_bound, lower_bound):
                    matrix[row][right_bound] = matrix[row + 1][right_bound]
                for col in range(right_bound, left_bound, -1):
                    matrix[lower_bound][col] = matrix[lower_bound][col - 1]
                for row in range(lower_bound, upper_bound, -1):
                    matrix[row][left_bound] = matrix[row - 1][left_bound]
                matrix[upper_bound + 1][left_bound] = initial_element
            upper_bound += 1
            left_bound += 1
            lower_bound -= 1
            right_bound -= 1
        return matrix

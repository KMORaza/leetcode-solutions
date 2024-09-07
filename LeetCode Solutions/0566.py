class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        original_rows = len(mat)
        original_cols = len(mat[0])
        if original_rows * original_cols != r * c:
            return mat
        flat_list = [num for row in mat for num in row]
        reshaped_matrix = []
        for i in range(r):
            reshaped_matrix.append(flat_list[i * c:(i + 1) * c])
        return reshaped_matrix

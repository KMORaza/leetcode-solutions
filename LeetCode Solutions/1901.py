from typing import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        n, m = len(mat), len(mat[0])
        left, right = 0, m - 1
        while left <= right:
            mid_col = (left + right) // 2
            max_row = 0
            for row in range(n):
                if mat[row][mid_col] > mat[max_row][mid_col]:
                    max_row = row
            max_val = mat[max_row][mid_col]
            is_left_greater = (mid_col > 0 and mat[max_row][mid_col - 1] > max_val)
            is_right_greater = (mid_col < m - 1 and mat[max_row][mid_col + 1] > max_val)
            if not is_left_greater and not is_right_greater:
                return [max_row, mid_col]
            elif is_left_greater:
                right = mid_col - 1
            else:
                left = mid_col + 1
        return []

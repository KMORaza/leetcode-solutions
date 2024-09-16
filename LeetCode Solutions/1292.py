from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (mat[i-1][j-1]
                                + prefix[i-1][j]
                                + prefix[i][j-1]
                                - prefix[i-1][j-1])
        def get_sum(x1, y1, x2, y2):
            return (prefix[x2+1][y2+1]
                    - prefix[x1][y2+1]
                    - prefix[x2+1][y1]
                    + prefix[x1][y1])
        def is_valid(side_length):
            for i in range(m - side_length + 1):
                for j in range(n - side_length + 1):
                    if get_sum(i, j, i + side_length - 1, j + side_length - 1) <= threshold:
                        return True
            return False
        low, high = 0, min(m, n)
        while low <= high:
            mid = (low + high) // 2
            if is_valid(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
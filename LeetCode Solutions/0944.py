from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_columns = len(strs[0])
        num_rows = len(strs)
        delete_count = 0
        for col in range(num_columns):
            for row in range(1, num_rows):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break
        return delete_count

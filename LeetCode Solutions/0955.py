class Solution:
    def minDeletionSize(self, strs):
        num_strings = len(strs)
        deletions_needed = 0
        column_sorted = [False] * (num_strings - 1)
        for col_index in range(len(strs[0])):
            row_index = 0
            while row_index + 1 < num_strings:
                if not column_sorted[row_index] and strs[row_index][col_index] > strs[row_index + 1][col_index]:
                    deletions_needed += 1
                    break
                row_index += 1
            if row_index + 1 == num_strings:
                for row_index in range(num_strings - 1):
                    column_sorted[row_index] = column_sorted[row_index] or strs[row_index][col_index] < strs[row_index + 1][col_index]
        return deletions_needed

import bisect
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        def max_sum_1d(arr, k):
            prefix_sums = [0]
            curr_sum = 0
            max_sum = float('-inf')
            for num in arr:
                curr_sum += num
                idx = bisect.bisect_left(prefix_sums, curr_sum - k)
                if idx < len(prefix_sums):
                    max_sum = max(max_sum, curr_sum - prefix_sums[idx])
                bisect.insort(prefix_sums, curr_sum)
            return max_sum
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for row in range(m):
                    row_sum[row] += matrix[row][right]
                max_sum = max(max_sum, max_sum_1d(row_sum, k))
        return max_sum
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        from collections import defaultdict
        def count_subarrays_with_sum(arr: List[int], target: int) -> int:
            prefix_sum_count = defaultdict(int)
            prefix_sum_count[0] = 1
            current_sum = 0
            count = 0
            for num in arr:
                current_sum += num
                if (current_sum - target) in prefix_sum_count:
                    count += prefix_sum_count[current_sum - target]
                prefix_sum_count[current_sum] += 1
            return count
        rows = len(matrix)
        cols = len(matrix[0])
        result = 0
        for top in range(rows):
            col_sum = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    col_sum[col] += matrix[bottom][col]
                result += count_subarrays_with_sum(col_sum, target)
        return result

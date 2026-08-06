class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        prefix_sum = 0

        for i in range(1, n + 1):
            prefix_sum += i
            suffix_sum = total_sum - prefix_sum + i

            if prefix_sum == suffix_sum:
                return i

        return -1
class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        def count_while_sorting(prefix_sums, start, end):
            if end - start <= 1:
                return 0
            mid = (start + end) // 2
            count = count_while_sorting(prefix_sums, start, mid) + count_while_sorting(prefix_sums, mid, end)
            j = k = mid
            for i in range(start, mid):
                while j < end and prefix_sums[j] - prefix_sums[i] < lower:
                    j += 1
                while k < end and prefix_sums[k] - prefix_sums[i] <= upper:
                    k += 1
                count += k - j
            prefix_sums[start:end] = sorted(prefix_sums[start:end])
            return count
        return count_while_sorting(prefix_sums, 0, len(prefix_sums))

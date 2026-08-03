class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        from collections import defaultdict
        groups = defaultdict(list)
        for num in nums:
            ds = digit_sum(num)
            groups[ds].append(num)

        max_sum = -1
        for group in groups.values():
            if len(group) >= 2:
                group.sort(reverse=True)
                max_sum = max(max_sum, group[0] + group[1])

        return max_sum
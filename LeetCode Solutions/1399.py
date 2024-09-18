class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(x: int) -> int:
            return sum(int(d) for d in str(x))
        group_counts = {}
        for i in range(1, n + 1):
            s = digit_sum(i)
            if s in group_counts:
                group_counts[s] += 1
            else:
                group_counts[s] = 1
        max_size = max(group_counts.values())
        return sum(1 for count in group_counts.values() if count == max_size)

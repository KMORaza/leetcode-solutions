from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        max_count = max(freq.values())
        max_count_tasks = sum(1 for count in freq.values() if count == max_count)
        min_intervals = (max_count - 1) * (n + 1) + max_count_tasks
        return max(min_intervals, len(tasks))

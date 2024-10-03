from collections import Counter
from typing import List
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_count = Counter(tasks)
        total_rounds = 0
        for count in task_count.values():
            if count == 1:
                return -1
            total_rounds += (count + 2) // 3
        return total_rounds
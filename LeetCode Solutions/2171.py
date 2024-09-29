from typing import List
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total_beans = sum(beans)
        min_removals = float('inf')
        n = len(beans)
        for i in range(n):
            current_beans = beans[i] * (n - i)
            removals = total_beans - current_beans
            min_removals = min(min_removals, removals)
        return min_removals

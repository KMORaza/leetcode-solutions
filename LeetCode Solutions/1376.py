from typing import List
from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                graph[mgr].append(employee)
        def dfs(employee: int) -> int:
            if not graph[employee]:
                return 0
            max_time = 0
            for subordinate in graph[employee]:
                max_time = max(max_time, dfs(subordinate))
            return informTime[employee] + max_time
        return dfs(headID)
